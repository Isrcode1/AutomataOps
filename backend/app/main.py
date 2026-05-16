from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine
from app.database import models
from app.routes import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutomataOps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    return {"message": "AutomataOps Backend Running"}
