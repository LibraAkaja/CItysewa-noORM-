import axios from 'axios';

// Base axios instance
const api = axios.create({
    baseURL: 'https://citysewa2.onrender.com/api/v1', //Backend url
});

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("token");
        if(token){
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

/* Accounts */

//Customer registration info post and login
export const customerLogin = (data) =>
    api.post("/accounts/customer/login",data);

export const customerRegister = (data) => 
    api.post("/accounts/customer/register",data);

//Customer info fetch
export const fetchCustomers = () => 
    api.get("/accounts/customer");

export const fetchCustomerById = (id) => 
    api.get(`/accounts/customer/${id}`);

//Provider registration info post and login
export const providerLogin = (data) =>
    api.post("/accounts/provider/login",data);

export const providerRegister = (data) => 
    api.post("/accounts/provider/register",data);

//Provider info fetch
export const fetchProviders = () => 
    api.get("/accounts/provider");

export const fetchProviderById = (id) => 
    api.get(`/accounts/provider/${id}`);

//Provider verification
export const submitForVerification = (data) =>
    api.post("/accounts/provider/submit-verification",data);

//Provider verification in Admin side
export const fetchVerificationData = () => 
    api.get("/accounts/provider/verification-data");

export const fetchVerificationDataById = (id) =>
    api.get(`/accounts/provider/verification-data/${id}`);

export const updateVerificationData = (id, data) => 
    api.patch(`/accounts/provider/verification-data/${id}`,daat);

//Admin login/register
export const adminLogin = (data) => 
    api.post("/accounts/admin/login",data);

export const adminRegister = (data) =>
    api.post("/accounts/admin/register",data);

export default api;