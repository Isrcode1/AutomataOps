from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from app.database.database import get_db
from app.database.models import Task

router = APIRouter()

class TaskCreate(BaseModel):
    title: str
    priority: Optional[str] = "normal"

class TaskUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None

@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, priority=task.priority)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/stats/summary")
def task_stats(db: Session = Depends(get_db)):
    total = db.query(Task).count()
    pending = db.query(Task).filter(Task.status == "pending").count()
    completed = db.query(Task).filter(Task.status == "completed").count()
    failed = db.query(Task).filter(Task.status == "failed").count()
    return {
        "total": total,
        "pending": pending,
        "completed": completed,
        "failed": failed
    }

@router.get("/")
def list_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Task)
    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    if search:
        query = query.filter(Task.title.contains(search))
    total = query.count()
    tasks = query.offset((page - 1) * limit).limit(limit).all()
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "results": tasks
    }

@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}")
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if update.status:
        task.status = update.status
    if update.priority:
        task.priority = update.priority
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted"}
