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

    useEffect(() => {
        if (isLoggedIn) {
            navigate('/dashboard');
        }
    }, [isLoggedIn, navigate]);

    useEffect(() => {
        return () => {
            dispatch(clearError());
        };
    }, [dispatch]);

    const handleChange = (e) => {
        const { name, value } = e.target;

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

        if (name === 'password' || name === 'confirmPassword') {
            setPasswordError('');
        }
    };

    const validateForm = () => {
        if (formData.password !== formData.confirmPassword) {
            setPasswordError('As senhas não coincidem');
            return false;
        }

        if (formData.password.length < 8) {
            setPasswordError('A senha deve ter pelo menos 8 caracteres');
            return false;
        }

        if (!/[A-Z]/.test(formData.password)) {
            setPasswordError('A senha deve conter pelo menos uma letra maiúscula');
            return false;
        }

        if (!/[a-z]/.test(formData.password)) {
            setPasswordError('A senha deve conter pelo menos uma letra minúscula');
            return false;
        }

        if (!/\d/.test(formData.password)) {
            setPasswordError('A senha deve conter pelo menos um número');
            return false;
        }

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

        const { confirmPassword, ...userData } = formData;

        try {
            await dispatch(registerUser(userData)).unwrap();
            navigate('/dashboard');
        } catch (err) {
            console.error('Registration failed:', err);
        }
    };

    return (
        <div className="auth-layout">
            <div className="auth-left">
                <div className="hero-content">
                    <h1 className="hero-title">
                        GERENCIE <span className="text-white">O</span> SEU<br />
                        PASSE DE FORMA<br />
                        <span className="text-blue">ONLINE</span>
                    </h1>
                    <div className="hero-illustration"></div>
                </div>
            </div>

            <div className="auth-right">
                <div className="auth-card">
                    <h2 className="card-title">Bem Vindo(a)</h2>
                    <p className="card-subtitle">
                        Crie sua conta e <span className="text-yellow">gerencie</span> o seu passe <span className="text-blue">rapidamente</span>.
                    </p>
                    <p className="card-note">A partir do teu telemóvel</p>

                    {error && (
                        <div className="error-box">
                            <span>{error}</span>
                        </div>
                    )}

                    {passwordError && (
                        <div className="error-box">
                            <span>{passwordError}</span>
                        </div>
                    )}

                    <form onSubmit={handleSubmit} className="auth-form">
                        <div className="form-field">
                            <input
                                type="text"
                                name="full_name"
                                value={formData.full_name}
                                onChange={handleChange}
                                placeholder="Nome Completo"
                                disabled={loading}
                                required
                            />
                        </div>

                        <div className="form-field">
                            <input
                                type="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                placeholder="Email"
                                disabled={loading}
                                required
                            />
                        </div>

                        <div className="form-field">
                            <input
                                type="text"
                                name="nif"
                                value={formData.nif}
                                onChange={handleChange}
                                placeholder="NIF (9 dígitos)"
                                disabled={loading}
                                required
                                maxLength="9"
                                pattern="\d{9}"
                            />
                        </div>

                        <div className="form-field">
                            <input
                                type="tel"
                                name="phone"
                                value={formData.phone}
                                onChange={handleChange}
                                placeholder="Telefone (opcional)"
                                disabled={loading}
                            />
                        </div>

                        <div className="form-field">
                            <input
                                type="password"
                                name="password"
                                value={formData.password}
                                onChange={handleChange}
                                placeholder="Senha (mín. 8 caracteres)"
                                disabled={loading}
                                required
                                minLength="8"
                            />
                        </div>

                        <div className="form-field">
                            <input
                                type="password"
                                name="confirmPassword"
                                value={formData.confirmPassword}
                                onChange={handleChange}
                                placeholder="Confirmar senha"
                                disabled={loading}
                                required
                            />
                        </div>

                        <button type="submit" className="btn-primary" disabled={loading}>
                            {loading ? 'AGUARDE...' : 'CRIAR CONTA AGORA'}
                        </button>
                    </form>

                    <div className="social-section">
                        <p className="social-label">Ou Registe-se com</p>
                        <div className="social-icons">
                            <button type="button" className="social-icon" disabled>
                                <svg viewBox="0 0 24 24" width="20" height="20">
                                    <path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                                </svg>
                            </button>
                            <button type="button" className="social-icon" disabled>
                                <svg viewBox="0 0 24 24" width="20" height="20">
                                    <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                                    <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                                    <path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                                    <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                                </svg>
                            </button>
                            <button type="button" className="social-icon" disabled>
                                <svg viewBox="0 0 24 24" width="20" height="20">
                                    <path fill="currentColor" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                                </svg>
                            </button>
                        </div>
                    </div>

                    <div className="auth-link-box">
                        <Link to="/login" className="link-secondary">
                            Já possui uma conta? Clique aqui.
                        </Link>
                    </div>

                    <div className="auth-footer-legal">
                        <div className="footer-divider"></div>
                        <p className="legal-text">
                            Ao continuar, você concorda com os Termos de Uso e Política de Privacidade.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Register;
