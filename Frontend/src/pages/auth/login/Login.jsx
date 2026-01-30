import './../../../Style/Root.css';
import './../../../Style/Login.css';
import { useState } from 'react';
import {useNavigate} from "react-router-dom";
import { customerLogin, providerLogin } from '../../../api/client';

const Login = () => {
    // const [def, setDefault] = useState(1);  // 1 is for customers
    // const [login, setLogin] = useState(customerLogin);
    const [role, setRole] = useState("Customer");
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
    const handleRoleChange = (r) => {
        // setDefault(r);
        // setLogin(r ? customerLogin : providerLogin);
        setRole(r);
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            const login = (role === "Customer" ? customerLogin : providerLogin);
            const response = await login({
                email: credentials.email,
                password: credentials.password,
            });
            localStorage.setItem("token", response.data.access);
            navigate(role === "Customer" ? "/customer" : "/provider");
        } catch (err){
            setError("Invalid email or password");
            setCredentials({
                email: "",
                password: ""
            });
            console.error(err);
        }
    };
    return(
        <>
            <section className='login-as'>
                <div className="login-as-op" onClick={()=>handleRoleChange("Customer")} style={{background:`${role==="Customer" ? 'rgba(135, 206, 235, 0.75)': 'none'}`}}>Customer Login</div>
                <div className="login-as-op" onClick={()=>handleRoleChange("Provider")} style={{background:`${role==="Provider" ? 'rgba(135, 206, 235, 0.75)': 'none'}`}}>Provider Login</div>
            </section>
            <form className='login-form' onSubmit={handleSubmit}>
            <fieldset>
                <legend>{role==="Customer"? "Customer": "Provider"} Login</legend>
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
        </>
    );
};

export default Login;