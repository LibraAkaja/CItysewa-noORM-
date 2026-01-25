import Navbar from "../components/common/Navbar/NavBar";
import Footer from "../components/common/Footer/Footer";
import { Outlet } from "react-router-dom";
import Sidebar from "../components/admin/sidebar";
import { useState } from "react";

const AdminLayout = () => {
    const [activeSection, setActiveSection] = useState("Customers");
    return(
        <main className="admin-layout" style={{display:'flex', justifyContent:'space-evenly', alignItems:'center', border:'2px solid yellow', width:'100%'}}>
            <Sidebar setActiveSection={setActiveSection}/>
            <Outlet context={{activeSection}}/>
            <Footer type='admin'/>
        </main>
    );
};

export default AdminLayout;