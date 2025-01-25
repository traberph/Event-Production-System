import os
from app.models.static_ip import StaticIP


def flush_static_ips(static_ips):
    try:
        with open(os.environ.get("EPS_STATIC_LEASES_PATH"), "w") as f:
            for static_ip in static_ips:
                f.write(f"dhcp-host={static_ip.mac},{static_ip.ip},{static_ip.hostname}\n")
        return True
    except Exception as e:
        return False
