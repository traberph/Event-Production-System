from sqlalchemy import Integer, Column, String
from app.db import Base

class StaticIP(Base):

    __tablename__ = 'static_ip'

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True)
    mac = Column(String, unique=True)
    hostname = Column(String, unique=True)

    def __repr__(self):
        return f'<StaticIP(id={self.id}, ip={self.ip}, mac={self.mac}, hostname={self.hostname})>'

    def __str__(self):
        return f'<StaticIP(id={self.id}, ip={self.ip}, mac={self.mac}, hostname={self.hostname})>'

