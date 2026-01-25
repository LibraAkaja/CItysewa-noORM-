import {formatDate} from '../../utils/formatDate';

const BookingCard = ({booking}) => {
    return(
        <section className='booking-card'>
            <h4>{booking.service?.title}</h4>
            <p>{formatDate(booking.booking_date)} at {booking.booking_time}</p>
            <p>{booking.customer_address}</p>
            <p>
                <strong>Status: </strong>{' '}
                <span className={`status status-${booking.status}`}>{booking.status}</span>
            </p>
            {booking.status === 'pending' && (
                <button className='cancel-btn'>Cancel Booking</button>
            )}
        </section>
    );
};

export default BookingCard;