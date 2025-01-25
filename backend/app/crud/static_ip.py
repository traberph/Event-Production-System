from sqlalchemy.orm import Session
from app.models.static_ip import StaticIP
from app.schemas.static_ip import StaticIPCreate, StaticIPUpdate

def select_static_ips(db: Session):
    return db.query(StaticIP).all()

def insert_static_ip(db: Session, static_ip: StaticIPCreate):
    db_static_ip = StaticIP(ip=str(static_ip.ip), mac=static_ip.mac, hostname=static_ip.hostname)
    db.add(db_static_ip)
    db.commit()
    db.refresh(db_static_ip)
    return db_static_ip

def update_static_ip(db: Session, static_ip_id: int, static_ip: StaticIPUpdate):
    db_static_ip = db.query(StaticIP).filter(StaticIP.id == static_ip_id).first()
    if db_static_ip is None:
        return None
    for key, value in static_ip.dict().items():
        setattr(db_static_ip, key, value)
    db.commit()
    db.refresh(db_static_ip)
    return db_static_ip
