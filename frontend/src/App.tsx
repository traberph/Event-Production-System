import { useState, useEffect } from "react";
import axios from "axios";
import {IIp} from "./interfaces.ts";




const App = () => {
    const [ips, setIps] = useState([]);
    const [search, setSearch] = useState("");

    useEffect(() => {
        // Fetch data from the backend
        const fetchData = async () => {
            try {
                
                const response = await axios.get("api/lease/");
                setIps(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchData();
    }, []);

    // Filter the data based on the search input
    const filteredIps = ips.filter(
        (ip: IIp) =>
            ip.ip_address.includes(search) ||
            ip.mac_address.includes(search) ||
            (ip.hostname && ip.hostname.toLowerCase().includes(search.toLowerCase()))
    );

    return (
        <div className="p-6 min-h-screen bg-gray-100">
            <h1 className="text-2xl font-bold mb-4">Event Production System - ICF Singen</h1>
            <h2 className="">DHCP Leases</h2>

            <div className="my-9">
                <input
                    type="text"
                    placeholder="Search by IP, MAC, or Hostname"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    className="p-2 rounded border border-gray-300"
                />
            </div>

            <div className="bg-white rounded shadow overflow-hidden">
                <table className="w-full border-collapse">
                    <thead className="bg-gray-50">
                    <tr>
                        <th className="text-left py-3 px-4 border-b">IP Address</th>
                        <th className="text-left py-3 px-4 border-b">MAC Address</th>
                        <th className="text-left py-3 px-4 border-b">Hostname</th>
                    </tr>
                    </thead>
                    <tbody>
                    {filteredIps.length > 0 ? (
                        filteredIps.map((ip: IIp, index) => (
                            <tr key={index} className="border-b">
                                <td className="py-3 px-4">{ip.ip_address}</td>
                                <td className="py-3 px-4">{ip.mac_address}</td>
                                <td className="py-3 px-4">{ip.hostname || "N/A"}</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan={3} className="text-center py-4">No results found</td>
                        </tr>
                    )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default App;