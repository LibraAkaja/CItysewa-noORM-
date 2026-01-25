import './../../../Style/Root.css';
import './../../../Style/Login.css';
import { useState } from 'react';
import {useNavigate} from "react-router-dom";
import { adminLogin } from '../../../api/client';

const Login = () => {
    const [credentials, setCredentials] = useState({
        email: "",
        password: "",
    });
    const [error, setError] = useState("");
    const navigate = useNavigate();
    const handleChange = (e) => {
        setCredentials({
            ...credentials,
            [e.target.name]: e.target.value,
        });
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            const response = await adminLogin({
                email: credentials.email,
                password: credentials.password,
            });
            localStorage.setItem("token", response.data.access);
            navigate("/admin");
        } catch (err){
            setError("Invalid email or password");
            console.error(err);
        }
    };
    return(
        <form className='login-admin-form' onSubmit={handleSubmit}>
            <fieldset>
                <legend>Admin Login</legend>
                {error && <p className='error'>{error}</p>}
                <span>
                    <label htmlFor="username-email">Username/Email</label>
                    <input type="text" id="username-email" name="email" value={credentials.email} onChange={handleChange} required/>  
                </span>
                <span>
                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" name="password" value={credentials.password} onChange={handleChange} required/>
                </span>
                <button type="submit">Login</button>
            </fieldset>
        </form>
    );
};

export default Login;