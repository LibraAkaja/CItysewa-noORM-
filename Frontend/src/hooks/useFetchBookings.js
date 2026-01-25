// import { useState, useEffect } from "react";
// import { fetchBookings } from "../api/client";

// const useFetchBookings = () => {
//     const [bookings, setBookings] = useState([]);
//     const [loading, setLoading] = useState(true);
//     const [error, setError] = useState(null);

//     useEffect(()=>{
//         fetchBookings()
//         .then((res) => {
//             setBookings(res.data);
//         })
//         .catch((err)=>{
//             setError(err);
//         })
//         .finally(()=>{
//             setLoading(false);
//         });
//     },[]);

//     return {bookings, loading, error};
// }

// export default useFetchBookings;