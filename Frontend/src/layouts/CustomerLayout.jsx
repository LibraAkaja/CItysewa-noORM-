import { Outlet } from "react-router-dom";
import Navbar from "../components/common/Navbar/NavBar";
import Footer from "../components/common/Footer";

const CustomerLayout = () => {
    return(
        <main style={{display:'flex', justifyContent:'space-evenly', alignItems:'center', width:'100%', border:'2px solid white'}}>
            <Navbar type='customer'/>
            <section><Outlet/></section>
            {/* <Footer/> */}
        </main>
    );
};

export default CustomerLayout;