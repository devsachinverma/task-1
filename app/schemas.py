from pydantic import BaseModel
from typing import List

class WebhookData(BaseModel):
    id: int
    data: str

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CampaignBase(BaseModel):
    title: str
    description: str

class CampaignCreate(CampaignBase):
    pass
