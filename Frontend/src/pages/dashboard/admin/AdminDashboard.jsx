import { useState } from "react";
import "../../../Style/Dashboard.css";
import Customers from "./CustomerTable";
import Providers from "./ProviderTable";
// import { filteredProviders } from "./ProviderTable";
import { useOutletContext } from "react-router-dom";

const AdminDashboard = (e) => {
    const [searchBy, setSearchBy] = useState("Id");
    const [searchText, setSearchText] = useState("");
    const {activeSection} = useOutletContext();
    const renderContext = () => {
        switch(activeSection){
            case "Customers":
                return <Customers searchText={searchText} searchBy={searchBy}/>
            case "Providers":
                return <Providers searchText={searchText} searchBy={searchBy}/>
            default:
                return null;
        }
    };
    const handleChange = (e) => {
        setSearchBy(e.target.value);
    }
    return(
        <section className="admin-dashboard">
            <h1>Admin Dashboard</h1>
            <input type="text" placeholder={`Search by ${searchBy}`} value={searchText} id="searchBar" onChange={(e)=>setSearchText(e.target.value)}/>
            <select value={searchBy} name="searchBy" onChange={handleChange}>
                <option disabled hidden value={""}>Search by</option>
                <option value={"Id"}>Id</option>
                <option value={"First Name"}>First Name</option>
                <option value={"Last Name"}>Last Name</option>
            </select>
            {renderContext()}
        </section>
    );
};

export default AdminDashboard;