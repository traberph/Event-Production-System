interface IIp {
    ip_lease_id: number;
    ip_address: string;
    mac_address: string;
    hostname?: string; // Using optional chaining for hostname as it might be null or undefined
}

export type { IIp };