from fastapi import FastAPI, BackgroundTasks, HTTPException, Query, Header,Depends
from sqlalchemy.orm import Session
from app import models, database, schemas, tasks, utils
from typing import List, Optional

app = FastAPI()

# Dependency for database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/webhook")
async def receive_webhook(data: schemas.WebhookData, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Process webhook data and store it in the database
    background_tasks.add_task(tasks.process_webhook_data, data, db)
    return {"message": "Data received"}

@app.get("/data")
async def get_data(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = utils.get_paginated_data(db, offset, limit)
    return {"data": data}

@app.get("/sync/{source}")
async def sync_data(source: str, db: Session = Depends(get_db)):
    if source == "crm":
        background_tasks.add_task(tasks.sync_crm_data, db)
    elif source == "marketing":
        background_tasks.add_task(tasks.sync_marketing_data, db)
    else:
        raise HTTPException(status_code=400, detail="Invalid source")
    return {"message": f"Sync started for {source}"}

@app.get("/tasks")
async def list_tasks():
    return {"tasks": tasks.get_running_tasks()}

@app.post("/tasks/cancel")
async def cancel_task(task_id: str):
    tasks.cancel_task(task_id)
    return {"message": "Task cancelled"}
