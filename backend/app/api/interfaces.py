import os

from fastapi import APIRouter
import psutil
import time
from typing import Dict, Any

router = APIRouter()
INTEREST = os.environ.get("EPS_INTEREST", "eth0,wlan0,wlp1s0").split(",")

@router.get("/")
async def get_network_stats():
    try:
        ips = psutil.net_if_addrs()
        stats = psutil.net_if_stats()

        # Get network IO counters before sleep
        counters_0 = psutil.net_io_counters(pernic=True)
        time.sleep(1)  # Wait for 1 second
        counters_1 = psutil.net_io_counters(pernic=True)

        filtered_stats: Dict[str, Any] = {}

        for interface in INTEREST:
            if interface in ips and interface in stats and interface in counters_0 and interface in counters_1:
                # Extract relevant information
                addr_info = ips[interface][0]
                ip_address = addr_info.address
                netmask = addr_info.netmask

                stat_info = stats[interface]
                is_up = stat_info.isup
                speed = stat_info.speed

                io_0 = counters_0[interface]
                io_1 = counters_1[interface]

                speed_sent = io_1.bytes_sent - io_0.bytes_sent
                speed_recv = io_1.bytes_recv - io_0.bytes_recv


                interface_stats = {
                    "ip_address": str(ip_address),
                    "netmask": str(netmask),
                    "status": "UP" if is_up else "DOWN",
                    "speed": speed,
                    "speed_sent": speed_sent,
                    "speed_recv": speed_recv,
                    "bytes_sent": io_1.bytes_sent,
                    "bytes_recv": io_1.bytes_recv

                }

                filtered_stats[interface] = interface_stats

        return {"network_stats": filtered_stats}

    except Exception as e:
        return {"error": str(e)}, 500
