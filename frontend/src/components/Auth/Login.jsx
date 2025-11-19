/**
 * Login Component
 */
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate, Link } from 'react-router-dom';
import { loginUser, clearError } from '../../store/authSlice';
import './Auth.css';

const Login = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { loading, error, isLoggedIn } = useSelector((state) => state.auth);

    // Redirect if already logged in
    useEffect(() => {
        if (isLoggedIn) {
            navigate('/dashboard');
        }
    }, [isLoggedIn, navigate]);

    // Clear error when component unmounts
    useEffect(() => {
        return () => {
            dispatch(clearError());
        };
    }, [dispatch]);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Basic validation
        if (!formData.email || !formData.password) {
            return;
        }

        try {
            await dispatch(loginUser(formData)).unwrap();
            navigate('/dashboard');
        } catch (err) {
            // Error is handled by Redux
            console.error('Login failed:', err);
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1 className="auth-title">CarrisPlus</h1>
                <h2 className="auth-subtitle">Login</h2>

                {error && (
                    <div className="error-message">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="auth-form">
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            placeholder="seu@email.com"
                            disabled={loading}
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            placeholder="••••••••"
                            disabled={loading}
                        />
                    </div>

                    <button
                        type="submit"
                        className="btn-primary"
                        disabled={loading}
                    >
                        {loading ? 'A entrar...' : 'Entrar'}
                    </button>
                </form>

                <div className="auth-footer">
                    <p>
                        Não tem conta?{' '}
                        <Link to="/register" className="auth-link">
                            Registe-se aqui
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Login;
