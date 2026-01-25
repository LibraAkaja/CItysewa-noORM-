import BrowseServices from "../../components/services/BrowseServices";
import "../../Style/Services.css";

const Services = () => {
    return(
        <section className="services">
            {/* <h1>Services</h1> */}
            <BrowseServices from="services"/>
        </section>
    );
};

export default Services;