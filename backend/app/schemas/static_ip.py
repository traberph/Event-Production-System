import ipaddress
import os

from pydantic import BaseModel, BeforeValidator, ValidationError, field_validator
from pydantic.networks import IPv4Address
from typing import Optional


class StaticIPBase(BaseModel):
    ip: IPv4Address
    mac: str
    hostname: Optional[str]

    @field_validator("ip")
    def check_ip(cls, value):
        ip = value
        network = ipaddress.IPv4Network(os.environ.get("EPS_STATIC_NETWORK"))
        if ip not in network:
            raise ValueError(f"IP address {ip} is not in the allowed network {network}")
        return ip

class StaticIPCreate(StaticIPBase):
    pass

class StaticIPUpdate(BaseModel):
    ip: Optional[IPv4Address] = None
    mac: Optional[str] = None
    hostname: Optional[str] = None


class StaticIPResponse(StaticIPBase):
    id: int
    
    
    
