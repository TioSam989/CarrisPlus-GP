import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import axios from 'axios';
import Toast from '../Toast/Toast';
import './Auth.css';

const ResetPassword = () => {
    const [searchParams] = useSearchParams();
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        password: '',
        confirmPassword: ''
    });
    const [loading, setLoading] = useState(false);
    const [verifying, setVerifying] = useState(true);
    const [error, setError] = useState('');
    const [tokenValid, setTokenValid] = useState(false);
    const [email, setEmail] = useState('');
    const [showToast, setShowToast] = useState(false);
    const [toastMessage, setToastMessage] = useState('');

    const token = searchParams.get('token');
    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

    useEffect(() => {
        // Verify token on component mount
        const verifyToken = async () => {
            if (!token) {
                setError('Token de redefinição inválido ou ausente');
                setVerifying(false);
                return;
            }

            try {
                const response = await axios.post(`${API_URL}/api/auth/verify-reset-token`, {
                    token
                });

                if (response.data.valid) {
                    setTokenValid(true);
                    setEmail(response.data.email);
                }
            } catch (err) {
                setError(err.response?.data?.error || 'Token inválido ou expirado');
            } finally {
                setVerifying(false);
            }
        };

        verifyToken();
    }, [token, API_URL]);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
        setError('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        // Validate passwords match
        if (formData.password !== formData.confirmPassword) {
            setError('As senhas não coincidem');
            return;
        }

        // Validate password strength
        if (formData.password.length < 8) {
            setError('A senha deve ter pelo menos 8 caracteres');
            return;
        }

        setLoading(true);

        try {
            const response = await axios.post(`${API_URL}/api/auth/reset-password`, {
                token,
                password: formData.password
            });

            setToastMessage(response.data.message);
            setShowToast(true);

            // Redirect to login after 2 seconds
            setTimeout(() => {
                navigate('/login', {
                    state: { message: 'Senha redefinida com sucesso! Faça login com sua nova senha.' }
                });
            }, 2000);

        } catch (err) {
            setError(err.response?.data?.error || 'Erro ao redefinir senha');
        } finally {
            setLoading(false);
        }
    };

    if (verifying) {
        return (
            <div className="auth-layout">
                <div className="auth-left">
                    <div className="hero-content">
                        <h1 className="hero-title">
                            REDEFINA <span className="text-white">A</span> SUA<br />
                            SENHA DE FORMA<br />
                            <span className="text-blue">SEGURA</span>
                        </h1>
                        <div className="hero-illustration"></div>
                    </div>
                </div>

                <div className="auth-right">
                    <div className="auth-card">
                        <div className="loading-spinner">
                            <p>Verificando token...</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    if (!tokenValid) {
        return (
            <div className="auth-layout">
                <div className="auth-left">
                    <div className="hero-content">
                        <h1 className="hero-title">
                            REDEFINA <span className="text-white">A</span> SUA<br />
                            SENHA DE FORMA<br />
                            <span className="text-blue">SEGURA</span>
                        </h1>
                        <div className="hero-illustration"></div>
                    </div>
                </div>

                <div className="auth-right">
                    <div className="auth-card">
                        <h2 className="card-title">Token Inválido</h2>
                        <div className="error-box">
                            <span>{error}</span>
                        </div>
                        <div className="auth-link-box">
                            <Link to="/forgot-password" className="link-secondary">
                                Solicitar novo link de redefinição
                            </Link>
                        </div>
                        <div className="auth-link-box">
                            <Link to="/login" className="link-secondary">
                                Voltar para login
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <>
            {showToast && (
                <Toast
                    message={toastMessage}
                    type="success"
                    onClose={() => setShowToast(false)}
                />
            )}
            <div className="auth-layout">
                <div className="auth-left">
                    <div className="hero-content">
                        <h1 className="hero-title">
                            REDEFINA <span className="text-white">A</span> SUA<br />
                            SENHA DE FORMA<br />
                            <span className="text-blue">SEGURA</span>
                        </h1>
                        <div className="hero-illustration"></div>
                    </div>
                </div>

                <div className="auth-right">
                    <div className="auth-card">
                        <h2 className="card-title">Redefinir Senha</h2>
                        <p className="card-subtitle">
                            Crie uma <span className="text-yellow">nova senha</span> para sua conta: <span className="text-blue">{email}</span>
                        </p>

                        {error && (
                            <div className="error-box">
                                <span>{error}</span>
                            </div>
                        )}

                        <form onSubmit={handleSubmit} className="auth-form">
                            <div className="form-field">
                                <input
                                    type="password"
                                    name="password"
                                    value={formData.password}
                                    onChange={handleChange}
                                    placeholder="Nova Senha"
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
                                    placeholder="Confirmar Nova Senha"
                                    disabled={loading}
                                    required
                                    minLength="8"
                                />
                            </div>

                            <div className="password-requirements">
                                <p>A senha deve conter:</p>
                                <ul>
                                    <li>Mínimo de 8 caracteres</li>
                                    <li>Pelo menos uma letra maiúscula</li>
                                    <li>Pelo menos uma letra minúscula</li>
                                    <li>Pelo menos um número</li>
                                </ul>
                            </div>

                            <button type="submit" className="btn-primary" disabled={loading}>
                                {loading ? 'REDEFININDO...' : 'REDEFINIR SENHA'}
                            </button>
                        </form>

                        <div className="auth-link-box">
                            <Link to="/login" className="link-secondary">
                                Voltar para login
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
        </>
    );
};

export default ResetPassword;
