import "../../Style/Root.css";
import "../../Style/Sidebar.css";

const Sidebar = ({setActiveSection}) => {
    return(
        <section className="admin-sidebar">
            <button onClick={() => setActiveSection("Customers")}>Customers</button>
            <button onClick={() => setActiveSection("Providers")}>Providers</button>
            <button onClick={() => setActiveSection("Bookings")}>Bookings</button>
            <button onClick={() => setActiveSection("Services")}>Services</button>
            <button onClick={() => setActiveSection("Verification")}>Verification Request</button>
        </section>
    );
};

export default Sidebar;