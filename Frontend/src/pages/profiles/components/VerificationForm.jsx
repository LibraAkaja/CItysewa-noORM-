import "react-phone-number-input/style.css"
import PhoneInput from "react-phone-number-input";
import { useState } from "react";
// import { all } from "axios";

const VerificationForm = () => {
    const [formData, setFromData] = useState({
        id: "",
        phone_number: "",
        document_type: "",
        document_number: "",
        photo: "",
        document: ""
    });
    const [error, setError] = useState("");
    const [success, setSuccess] = useState("");
    const handleChange = (e) => {
        setFromData({
            ...formData,
            [e.target.name] : e.target.value
        });
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        setError("");
        setSuccess("");
        try{

        } catch(err) {
            
        } finally {

        }
    };
    return(
        <form className="verification-form" onSubmit={handleSubmit}>
            <h3>Verify Your Account</h3>
            <span>
                <label htmlFor="provider-id">ID</label>
                <input type="number" name="provider-id" value={formData.id} onChange={handleChange} required/>
            </span>
            <span>
                <label htmlFor="provider-photo">Upload Your Photo</label>
                <input type="file" name="provider-photo" accept=".jpg,.jpeg,.png" onChange={handleChange} required/>
            </span>
            <span>
                <label htmlFor="provider-phone">Phone Number</label>
                <PhoneInput international defaultCountry="NP" value={formData.phone_number} onChange={handleChange} placeholder="Enter phone number"/>
            </span>
            <span>
                <label htmlFor="provider-doc-type">Document Type</label>
                <select name="provider-doc-type" value={formData.document_type} onChange={handleChange}>
                    <option value={""} hidden disabled>Choose Document Type</option>
                    <option value={"NID"}>National Id</option>
                    <option value={"Citizen"}>Citizenship</option>
                    <option value={"Driving"}>Driving License</option>
                    <option value={"Voter"}>Voter Card</option>
                    <option value={"Pan"}>Pan Card</option>
                </select>
            </span>
            <span>
                <label htmlFor="provider-doc-number">Document Number</label>
                <input type="number" name="provider-doc-number" value={formData.document_number} onChange={handleChange} required/>
            </span>
            <span>
                <label htmlFor="provider-document">Attach Document</label>
                <input type="file" name="provider-document" accept=".jpg,.jpeg,.png,.pdf" onChange={handleChange} multiple required/>
            </span>
            <button type="submit">Submit</button>
        </form>
    );
};

export default VerificationForm;