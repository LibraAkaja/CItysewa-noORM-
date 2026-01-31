const VerificationDetails = ({data}) => {
    return(
        <section className="verification-details">
            <p><strong>Verification Status:</strong> {data.is_verified?"Verified":"Not verified"}</p>
            <p><strong>Id:</strong> {data.id}</p>
            <p><strong>Verified On:</strong> {data.verified_at}</p>
        </section>
    );
};

export default VerificationDetails;