/**
 * Main App Component
 */
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store/store';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Dashboard from './components/Dashboard';
import PrivateRoute from './utils/PrivateRoute';
import './App.css';

function App() {
    return (
        <Provider store={store}>
            <Router>
                <div className="App">
                    <Routes>
                        {/* Public routes */}
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />

                        {/* Protected routes */}
                        <Route
                            path="/dashboard"
                            element={
                                <PrivateRoute>
                                    <Dashboard />
                                </PrivateRoute>
                            }
                        />

                        {/* Default redirect */}
                        <Route path="/" element={<Navigate to="/login" />} />

                        {/* 404 */}
                        <Route path="*" element={<Navigate to="/login" />} />
                    </Routes>
                </div>
            </Router>
        </Provider>
    );
}

export default App;
