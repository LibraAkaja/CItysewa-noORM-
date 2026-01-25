import './../../../Style/Root.css';
import './../../../Style/Login.css';
import { useState } from 'react';
import {useNavigate} from "react-router-dom";
import { customerLogin, providerLogin } from '../../../api/client';

const Login = () => {
    const [def, setDefault] = useState(1);  // 1 is for customers
    const [login, setLogin] = useState(customerLogin);
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
    const handleClick = (r) => {
        setDefault(r);
        setLogin(r ? customerLogin : providerLogin);
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            const response = await login({
                email: credentials.email,
                password: credentials.password,
            });
            localStorage.setItem("token", response.data.access);
            navigate(def ? "/customer" : "/provider");
        } catch (err){
            setError("Invalid email or password");
            console.error(err);
        }
    };
    return(
        <>
            <section className='login-as'>
                <div className="login-as-op" onClick={()=>handleClick(1)} style={{background:`${def ? 'rgba(135, 206, 235, 0.75)': 'none'}`}}>Customer Login</div>
                <div className="login-as-op" onClick={()=>handleClick(0)} style={{background:`${!def ? 'rgba(135, 206, 235, 0.75)': 'none'}`}}>Provider Login</div>
            </section>
            <form className='login-form' onSubmit={handleSubmit}>
            <fieldset>
                <legend>Login</legend>
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