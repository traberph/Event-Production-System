from fastapi import FastAPI, Depends

from app.db import create_tables
from app.api import static_ip, lease

import dotenv
dotenv.load_dotenv()

openapi_tags = [
    {
        "name": "Static IPs",
        "description": "Manage static IPs"
    },
    {
        "name": "Leases",
        "description": "View leases"
    }
]

app = FastAPI(
    title="Event Production System",
    description="""
### Description
DHCP server management for an event production network running for example grandMA, ProPresenter, and other production software.
### Features  
View leases and assign static IPs.
    """,
    version="0.1",
    openapi_tags=openapi_tags
)
create_tables()


app.include_router(static_ip.router, prefix="/static_ip", tags=["Static IPs"])
app.include_router(lease.router, prefix="/lease", tags=["Leases"])

