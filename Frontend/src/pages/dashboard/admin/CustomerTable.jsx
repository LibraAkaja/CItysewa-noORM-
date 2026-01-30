import { useEffect, useState } from "react";
import {fetchCustomers} from "../../../api/client";

const Customers = () => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchBy, setSearchBy] = useState("Id");
    const handleChange = (e) => {
        setSearchBy(e.target.value);
    };

    useEffect(()=>{
        const loadCustomers = async () => {
            try{
                const response = await fetchCustomers();
                setCustomers(response.data);
            } catch (e) {
                setError("Failed to fetch customers");
                console.error(e);
            } finally {
                setLoading(false);
            }
        };
        loadCustomers();
    }, []);

    if (loading) return <p>Loading Customers ...</p>;
    if (error) return <p>{error}</p>

    return(
        <section className="customers">
            <h2>Customers</h2>
            <input type="text" placeholder={`Search by ${searchBy}`}/>
            <select value={searchBy} name="searchBy" onChange={handleChange}>
                <option disabled hidden value={""}>Search by</option>
                <option value={"Id"}>Id</option>
                <option value={"First Name"}>First Name</option>
                <option value={"Last Name"}>Last Name</option>
            </select>
            <table>
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>First name</th>
                        <th>Last name</th>
                        <th>Gender</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.slice().sort((a,b) => a.id - b.id).map((customer) => (
                        <tr key={customer.id}>
                            <td>{customer.id}</td>
                            <td>{customer.first_name}</td>
                            <td>{customer.last_name}</td>
                            <td>{customer.gender}</td>
                            <td>{customer.email}</td>
                        </tr>
                    ))}
                </tbody>  
            </table>
        </section>
    );
};

export default Customers;