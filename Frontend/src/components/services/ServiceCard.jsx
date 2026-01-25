import {useNavigate} from 'react-router-dom';

const ServiceCard = ({service}) => {
    const navigate = useNavigate();

    return(
        <section className='service-card'>
            <h3>{service.title}</h3>
            <p>{service.description}</p>
            <p>
                <strong>Price: </strong> Rs. {service.price} / {service.price_unit}
            </p>
            <p>
                <strong>Provider: </strong> {service.provider?.first_name}
            </p>
            <button onClick={()=>navigate(`/services/${service.id}`)}>Book Service</button>
        </section>
    );
};

export default ServiceCard;