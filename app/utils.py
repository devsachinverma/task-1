from sqlalchemy.orm import Session
from app.models import Customer, Campaign

def get_paginated_data(db: Session, offset: int, limit: int):
    customers = db.query(Customer).offset(offset).limit(limit).all()
    campaigns = db.query(Campaign).offset(offset).limit(limit).all()
    return {"customers": customers, "campaigns": campaigns}
