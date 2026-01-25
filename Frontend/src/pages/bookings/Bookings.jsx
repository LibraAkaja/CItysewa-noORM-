// import useFetchBookings from "../../hooks/useFetchBookings";
// import BookingCard from '../../components/bookings/BookingCard';

// const Bookings = () => {
//     const {bookings, loading, error} = useFetchBookings();

//     if (loading) return <p>Loading...</p>;
//     if(error) return <p>Error loading bookings</p>;

//     return(
//         <div>
//             {bookings.map((booking) => (
//                 <BookingCard key={booking.id} booking={booking}/>
//             ))}
//         </div>
//     );
// };

// export default Bookings;