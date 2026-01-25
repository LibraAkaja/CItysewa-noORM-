import "../../../Style/Dashboard.css";
import Customers from "./CustomerTable";
import { useOutletContext } from "react-router-dom";

const AdminDashboard = () => {
    const {activeSection} = useOutletContext();
    const renderContext = () => {
        switch(activeSection){
            case "Customers":
                return <Customers/>
            // Similarly put cases for other sidebar options
            default:
                return null;
        }
    };
    return(
        <section className="admin-dashboard">
            <h1>Admin Dashboard</h1>
            {renderContext()}
        </section>
    );
};

export default AdminDashboard;