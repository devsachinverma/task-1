import httpx

CRM_API_URL = "https://challenge.berrydev.ai/api/crm/customers"
MARKETING_API_URL = "https://challenge.berrydev.ai/api/marketing/campaigns"

async def fetch_crm_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(CRM_API_URL, headers={"X-API-Key": "<Your_GitHub_Username>"})
        response.raise_for_status()
        return response.json()

async def fetch_marketing_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(MARKETING_API_URL, headers={"X-API-Key": "<Your_GitHub_Username>"})
        response.raise_for_status()
        return response.json()
