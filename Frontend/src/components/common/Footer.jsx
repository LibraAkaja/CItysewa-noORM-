import { Link } from "react-router-dom";

const Footer = () => {
    return(
        <footer style={{border: '2px solid red', padding:'25px'}}>
            <h2>CitySewa</h2>
            <h5>All rights reserved</h5>
            <strong>For support and query:</strong>
            <a href="mailto:adhikaribiraj908@gmail.com" target="_blank">adhikaribiraj908@gmail.com</a>
            <Link to={"/login-admin"} style={{all:'unset', color:'white'}}>Admin Login</Link>
        </footer>
    );
};

export default Footer;