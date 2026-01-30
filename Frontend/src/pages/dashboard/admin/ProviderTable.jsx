import { useEffect, useState } from "react";
import {fetchProviders} from "../../../api/client";

const Providers = () => {
    const [providers, setProviders] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchBy, setSearchBy] = useState("Id");
    const handleChange = (e) => {
        setSearchBy(e.target.value);
    };

    useEffect(()=>{
        const loadProviders = async () => {
            try{
                const response = await fetchProviders();
                setProviders(response.data);
            } catch (e) {
                setError("Failed to fetch providers");
                console.error(e);
            } finally {
                setLoading(false);
            }
        };
        loadProviders();
    }, []);

    if (loading) return <p>Loading Providers ...</p>;
    if (error) return <p>{error}</p>

    return(
        <section className="providers">
            <h2>Providers</h2>
            <input type="text" placeholder={`Search by ${searchBy}`} id="searchBar"/>
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
                    {providers.slice().sort((a,b) => a.id - b.id).map((provider) => (
                        <tr key={provider.id}>
                            <td>{provider.id}</td>
                            <td>{provider.first_name}</td>
                            <td>{provider.last_name}</td>
                            <td>{provider.gender}</td>
                            <td>{provider.email}</td>
                        </tr>
                    ))}
                </tbody>  
            </table>
        </section>
    );
};

export default Providers;

// export const filteredProviders = () => {

//     return(
        
//     );
// };
    // providers.filter((p)=>{
    //     if(searchBy === 'Id') return String(p.id).includes(searchText);
    // });

