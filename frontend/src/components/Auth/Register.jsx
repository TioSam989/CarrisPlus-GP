/**
 * Register Component
 */
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate, Link } from 'react-router-dom';
import { registerUser, clearError } from '../../store/authSlice';
import './Auth.css';

const Register = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirmPassword: '',
        nif: '',
        full_name: '',
        phone: ''
    });

    const [passwordError, setPasswordError] = useState('');

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
        const { name, value } = e.target;

        // Special handling for NIF (only numbers, max 9 digits)
        if (name === 'nif') {
            const numericValue = value.replace(/\D/g, '').slice(0, 9);
            setFormData({
                ...formData,
                [name]: numericValue
            });
            return;
        }

        setFormData({
            ...formData,
            [name]: value
        });

        // Clear password error when typing
        if (name === 'password' || name === 'confirmPassword') {
            setPasswordError('');
        }
    };

    const validateForm = () => {
        // Password match validation
        if (formData.password !== formData.confirmPassword) {
            setPasswordError('As passwords não coincidem');
            return false;
        }

        // Password strength validation
        if (formData.password.length < 8) {
            setPasswordError('A password deve ter pelo menos 8 caracteres');
            return false;
        }

        if (!/[A-Z]/.test(formData.password)) {
            setPasswordError('A password deve conter pelo menos uma letra maiúscula');
            return false;
        }

        if (!/[a-z]/.test(formData.password)) {
            setPasswordError('A password deve conter pelo menos uma letra minúscula');
            return false;
        }

        if (!/\d/.test(formData.password)) {
            setPasswordError('A password deve conter pelo menos um número');
            return false;
        }

        // NIF validation
        if (formData.nif.length !== 9) {
            return false;
        }

        return true;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!validateForm()) {
            return;
        }

        // Prepare data (remove confirmPassword)
        const { confirmPassword, ...userData } = formData;

        try {
            await dispatch(registerUser(userData)).unwrap();
            navigate('/dashboard');
        } catch (err) {
            console.error('Registration failed:', err);
        }
    };

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1 className="auth-title">CarrisPlus</h1>
                <h2 className="auth-subtitle">Registo</h2>

                {error && (
                    <div className="error-message">
                        {error}
                    </div>
                )}

                {passwordError && (
                    <div className="error-message">
                        {passwordError}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="auth-form">
                    <div className="form-group">
                        <label htmlFor="full_name">Nome Completo *</label>
                        <input
                            type="text"
                            id="full_name"
                            name="full_name"
                            value={formData.full_name}
                            onChange={handleChange}
                            required
                            placeholder="João Silva"
                            disabled={loading}
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="email">Email *</label>
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
                        <label htmlFor="nif">NIF *</label>
                        <input
                            type="text"
                            id="nif"
                            name="nif"
                            value={formData.nif}
                            onChange={handleChange}
                            required
                            placeholder="123456789"
                            maxLength="9"
                            pattern="\d{9}"
                            disabled={loading}
                        />
                        <small className="form-hint">9 dígitos</small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="phone">Telefone (opcional)</label>
                        <input
                            type="tel"
                            id="phone"
                            name="phone"
                            value={formData.phone}
                            onChange={handleChange}
                            placeholder="+351912345678"
                            disabled={loading}
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password *</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            placeholder="••••••••"
                            minLength="8"
                            disabled={loading}
                        />
                        <small className="form-hint">
                            Mínimo 8 caracteres, incluindo maiúsculas, minúsculas e números
                        </small>
                    </div>

                    <div className="form-group">
                        <label htmlFor="confirmPassword">Confirmar Password *</label>
                        <input
                            type="password"
                            id="confirmPassword"
                            name="confirmPassword"
                            value={formData.confirmPassword}
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
                        {loading ? 'A registar...' : 'Registar'}
                    </button>
                </form>

                <div className="auth-footer">
                    <p>
                        Já tem conta?{' '}
                        <Link to="/login" className="auth-link">
                            Entre aqui
                        </Link>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Register;
