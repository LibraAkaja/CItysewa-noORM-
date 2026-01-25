import { Link } from "react-router-dom";
import BrowseServices from "../components/services/BrowseServices";

const Home = () => {
    return(
        <main>
            {/* <p>Hero Section</p> */}
            <section className="hero" style={{height:'40vh', border:'2px solid red'}}>
                Hero Section
            </section>
            <BrowseServices from="home"/>
            <p>Get involved section</p>
            <section className="get-involved" style={{display: 'flex'}}>
                <div className="be-customer" style={{width:'250px', aspectRatio:'1.5', border:'2px solid red', display:'flex', justifyContent:'center', alignItems: 'center'}}>Become a Customer</div>
                <div className="be-provider" style={{width:'250px', aspectRatio:'1.5', border:'2px solid red', display:'flex', justifyContent:'center', alignItems: 'center'}}>Become a Provider</div>
            </section>
            <p>User comments and views</p>
            <h3>See what our users have to say</h3>
            {/* Logic to map some of the user reviews and create appropriate no of divs */}
            <p>FAQs</p>
            <h3>Frequently Asked Questions</h3>
        </main>
    );
};

export default Home;