import os


def read_leases():
    with open(os.environ.get("EPS_LEASES_PATH"), 'r') as file:
        lines = file.readlines()

    leases = []

    for line in lines:
        parts = line.split()

        if len(parts) >= 5:
            mac_address = parts[1]
            ip_address = parts[2]
            hostname = parts[3]

            leases.append({
                'mac_address': mac_address,
                'ip_address': ip_address,
                'hostname': hostname
            })

    return leases
