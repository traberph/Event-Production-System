from fastapi import APIRouter
from app.filehandler.leases import read_leases

router = APIRouter()

@router.get("/")
def get_lease():
    return read_leases()