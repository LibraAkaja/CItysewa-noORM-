import React, { useState, useEffect, createContext, useContext } from 'react';
// import {jwtDecode} from "jwt-decode";

// 1. Create AuthContext
const AuthContext = createContext(null);

// 2. Provider component
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Load user from localStorage on mount
  useEffect(() => {
    const savedUser = localStorage.getItem('dummyUser');
    if (savedUser) setUser(JSON.parse(savedUser));
  }, []);

  const login = (username = 'testuser', role = 'customer') => {
    const dummyUser = { username, role };
    setUser(dummyUser);
    localStorage.setItem('dummyUser', JSON.stringify(dummyUser));
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('dummyUser');
  };

  // Return JSX inside the provider
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// 3. Custom hook to access auth
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within an AuthProvider');
  return context;
};