import { useEffect, useState } from "react";
import {fetchCustomers} from "../../../api/client";

const Customers = () => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchBy, setSearchBy] = useState("Id");
    const [shownIndex, setShownIndex] = useState(0);
    const PAGE_SIZE = 10;
    const customersOnDisplay = customers.slice(shownIndex, shownIndex + PAGE_SIZE);
    // Functions that show records on the table
    const showNextBatch = () => {
        setShownIndex(prev => prev + PAGE_SIZE < customers.length ? prev + PAGE_SIZE : prev);
    };
    const showPrevBatch = () => {
        setShownIndex(prev => prev - PAGE_SIZE >= 0 ? prev - PAGE_SIZE : 0);
    };
    // const showAll = () => {

    // };

    const handleChange = (e) => {
        setSearchBy(e.target.value);
    };

    useEffect(()=>{
        const loadCustomers = async () => {
            try{
                const response = await fetchCustomers();
                const sortedCustomers = response.data.slice().sort((a,b)=> a.id - b.id);
                setCustomers(sortedCustomers);
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
                    {customersOnDisplay.map(customer => (
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
            <span style={{display:'flex', flexDirection:'row', justifyContent:'space-evenly',marginTop:'8px'}}><p style={{opacity: shownIndex === 0 ? '0.5' : '1'}} onClick={showPrevBatch}>Prev</p><p style={{opacity: shownIndex + PAGE_SIZE >= customers.length ? '0.5' : '1'}} onClick={showNextBatch}>Next</p></span>
        </section>
    );
};

export default Customers;