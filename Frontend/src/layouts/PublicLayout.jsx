import Navbar from "../components/common/Navbar/NavBar";
import Footer from "../components/common/Footer";
import { Outlet } from "react-router-dom";
import "./../Style/Root.css";

const PublicLayout = () => {
    return(
        <main style={{display:'flex', justifyContent:'space-evenly', alignItems:'center', width:'100%', border:'2px solid white'}}>
            <Navbar type='public'/>
            {/* <section><Outlet/></section> */}
            <Footer/>
        </main>
    );
};

export default PublicLayout;