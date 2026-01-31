import { useEffect, useState } from "react";
import "../../Style/Profiles.css";
import { fetchVerificationData } from "../../api/client";
import VerificationForm from "./components/VerificationForm";
import VerificationDetails from "./components/VerificationDetails";

const ProviderProfile = () => {
    const [loading, setLoading] = useState(true);
    const [verification, setVerification] = useState(null);

    useEffect(()=>{
        const loadVerificationData = async () => {
            try{
                const res = await fetchVerificationData();
                setVerification(res.data);
            } catch(err) {
                console.log(err);
            } finally {
                setLoading(false);
            }
        };
        loadVerificationData();
    }, []);

    if(loading) {
        return <p>Loading Profile...</p>;
    }
    return(
        <section className="provider-profile">
            <h2>My Profile</h2>
            {!verification?.is_verified ? (<VerificationForm/>) : (<VerificationDetails data={verification}/>)}
        </section>
    );
};

export default ProviderProfile;