from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db import get_db
from app.filehandler.static_ip import flush_static_ips
from app.models.static_ip import StaticIP

from app.schemas.static_ip import StaticIPResponse, StaticIPCreate, StaticIPUpdate
from app.crud.static_ip import select_static_ips, insert_static_ip, update_static_ip

router = APIRouter()

@router.get("/", response_model=list[StaticIPResponse])
def get_static_ips(db: Session = Depends(get_db)):
    return select_static_ips(db)

@router.post("/", response_model=StaticIPResponse)
def post_static_ip(static_ip: StaticIPCreate, db: Session = Depends(get_db)):
    try:
        return insert_static_ip(db, static_ip)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Duplicate entry")

@router.put("/{static_ip_id}", response_model=StaticIPResponse)
def put_static_ip(static_ip_id: int, static_ip: StaticIPUpdate, db: Session = Depends(get_db)):
    try:
        return update_static_ip(db, static_ip_id, static_ip)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Duplicate entry")


@router.get("/flush")
def flush(db: Session = Depends(get_db)):
    """
    Flushes the static IPs to the leases file
    """
    static_ips = db.query(StaticIP).all()
    ok = flush_static_ips(static_ips)
    return {"message": "Flushed" if ok else "Failed to flush"}
