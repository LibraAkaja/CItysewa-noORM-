import Navbar from "../components/common/Navbar/NavBar";
import Footer from "../components/common/Footer/Footer";
import { Outlet } from "react-router-dom";
import "./../Style/Root.css";

const PublicLayout = () => {
    return(
        <main style={{display:'flex', justifyContent:'space-evenly', alignItems:'center', width:'100%', minHeight:'100vh', flexDirection:'column', border:'2px solid white'}}>
            <Navbar type='public'/>
            <section><Outlet/></section>
            <Footer type='public'/>
        </main>
    );
};

export default PublicLayout;