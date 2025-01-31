from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.db import create_tables
from app.api import static_ip, lease, interfaces
import os

if os.getenv('EPS_PROD') != 1:
    print("Loading .env file")
    import dotenv
    dotenv.load_dotenv()
else:
    print("Skipping .env file")

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
create_tables()

router = APIRouter()

#
#router.include_router(static_ip.router, prefix="/static_ip", tags=["Static IPs"])
router.include_router(lease.router, prefix="/lease", tags=["Leases"])
router.include_router(interfaces.router, prefix="/interface", tags=["Interfaces"])

app.include_router(router, prefix="/api")
