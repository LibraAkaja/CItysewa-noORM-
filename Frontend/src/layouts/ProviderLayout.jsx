import Navbar from "../components/common/Navbar/NavBar";
import Footer from "../components/common/Footer/Footer";
import { Outlet } from "react-router-dom";

const ProviderLayout = () => {
    return(
        <main style={{display:'flex', justifyContent:'space-evenly', alignItems:'center', width:'100%', border:'2px solid white'}}>
            <Navbar type='provider'/>
            <section><Outlet/></section>
            <Footer type='provider'/>
        </main>
    );
};

export default ProviderLayout;