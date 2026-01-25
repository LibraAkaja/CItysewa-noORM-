import { useState } from "react";
import {customerRegister, providerRegister} from "../../../api/client";
import "../../../Style/Register.css";
import { useNavigate } from "react-router-dom";

const Register = () => {
    const [formData, setFormData] = useState({
        email: "",
        // username: "",
        password: "",
        confirmPassword: "",
        role: "",
    });
    const [error, setError] = useState("");
    const [success, setSucceess] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        setSucceess("");
        if(formData.password !== formData.confirmPassword){
            setError("Passwords do not match");
            return;
        }
        try{
            if(formData.role !== "Admin" && formData.role === "Provider"){
                await providerRegister({
                    email: formData.email,
                    password: formData.password,
                });
            }
            if(formData.role !== "Admin" && formData.role === "Customer"){
                await customerRegister({
                    email: formData.email,
                    password: formData.password,
                });
            }
            setSucceess(`${formData.role} Registration Successful!`);
            navigate("/login");
        } catch (err) {
            setError(err.response?.data?.detail || "Registration Failed!");
        }
    };
    return(
        <form className="register-form" onSubmit={handleSubmit}>
            <fieldset>
                <legend>Register</legend>
                {error && <p className="error">{error}</p>}
                {success && <p className="success">{success}</p>}
                <span>
                    <label htmlFor="reg-email">Enter your email</label>
                    <input type="email" id="red-email" name="email" value={formData.email} onChange={handleChange} required/>
                </span>
                <span>
                    <span>
                        <label htmlFor="reg-fname">First Name</label>
                        <input type="text" id="reg-fname" name="first_name" required/>
                    </span>
                    <span>
                        <label htmlFor="reg-lname">Last Name</label>
                        <input type="text" id="reg-lname" name="last_name" required/>
                    </span>
                </span>
                <span>
                    <label htmlFor="reg-pass">Password</label>
                    <input type="password" id="reg-pass" name="password" value={formData.password} onChange={handleChange} required/>
                </span>
                <span>
                    <label htmlFor="reg-confirm-pass">Confirm Password</label>
                    <input type="password" id="reg-confirm-pass" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required/>
                </span>
                <span>
                    <label htmlFor="select-role">Your Role</label>
                    <select className="select-role" id="select-role" name="role" value={formData.role} onChange={handleChange}>
                        <option value={""} disabled hidden>Choose an option</option>
                        <option value={"Customer"}>Customer</option>
                        <option value={"Provider"}>Provider</option>
                    </select>
                </span>
                <button type="submit">Register</button>
            </fieldset>
        </form>
    );
};

export default Register;