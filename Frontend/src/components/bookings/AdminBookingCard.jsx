import {formatDate} from '../../utils/formatDate';

const AdminBookingCard = ({booking}) => {
    return(
        <section className='booking-card admin'>
            <h4>{booking.service?.title}</h4>
            <p>Customer: {booking.customer?.first_name}</p>
            <p>Provider: {booking.service?.provider?.first_name}</p>
            <p>{formatDate(booking.booking_date)} at {booking.booking_time}</p>
            <p>Status: {booking.status}</p>
            <p>Price: {booking.service?.price}</p>
            <button>Update Status</button>
        </section>
    );
};

export default AdminBookingCard;