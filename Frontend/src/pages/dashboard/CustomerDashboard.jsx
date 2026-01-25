import { useAuth } from '../../hooks/useAuth';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const CustomerDashboard = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  // Redirect if not logged in or wrong role
  useEffect(() => {
    if (!user || user.role !== 'customer') {
      navigate('/login'); // redirect to login page
    }
  }, [user, navigate]);

  if (!user || user.role !== 'customer') return null;

  return (
    <div>
      <h1>Customer Dashboard</h1>
      <p>Welcome, {user.username}</p>
    </div>
  );
};

export default CustomerDashboard;
