import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Toast from '../Toast/Toast';
import './Auth.css';

const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState(false);
    const [showToast, setShowToast] = useState(false);
    const [toastMessage, setToastMessage] = useState('');
    const [resetLink, setResetLink] = useState('');

    const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        if (!email) {
            setError('Por favor, insira seu email');
            setLoading(false);
            return;
        }

        try {
            const response = await axios.post(`${API_URL}/api/auth/forgot-password`, {
                email: email.trim().toLowerCase()
            });

            setSuccess(true);
            setToastMessage(response.data.message);
            setShowToast(true);

            // For development: show reset link
            if (response.data.reset_link) {
                setResetLink(response.data.reset_link);
            }

        } catch (err) {
            setError(err.response?.data?.error || 'Erro ao processar solicitação');
        } finally {
            setLoading(false);
        }
    };

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
                            RECUPERE <span className="text-white">A</span> SUA<br />
                            SENHA DE FORMA<br />
                            <span className="text-blue">SEGURA</span>
                        </h1>
                        <div className="hero-illustration"></div>
                    </div>
                </div>

                <div className="auth-right">
                    <div className="auth-card">
                        <h2 className="card-title">Esqueceu a Senha?</h2>
                        <p className="card-subtitle">
                            Insira seu email e enviaremos <span className="text-yellow">instruções</span> para redefinir sua senha.
                        </p>

                        {!success ? (
                            <>
                                {error && (
                                    <div className="error-box">
                                        <span>{error}</span>
                                    </div>
                                )}

                                <form onSubmit={handleSubmit} className="auth-form">
                                    <div className="form-field">
                                        <input
                                            type="email"
                                            name="email"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            placeholder="Email"
                                            disabled={loading}
                                            required
                                        />
                                    </div>

                                    <button type="submit" className="btn-primary" disabled={loading}>
                                        {loading ? 'ENVIANDO...' : 'ENVIAR INSTRUÇÕES'}
                                    </button>
                                </form>
                            </>
                        ) : (
                            <div className="success-message">
                                <div className="success-icon">✓</div>
                                <p className="success-text">
                                    Se uma conta existe com este email, você receberá instruções para redefinir sua senha.
                                </p>
                                {resetLink && (
                                    <div className="dev-reset-link">
                                        <p><strong>Link de Reset (Desenvolvimento):</strong></p>
                                        <a href={resetLink} className="reset-link-dev">
                                            Clique aqui para redefinir sua senha
                                        </a>
                                    </div>
                                )}
                            </div>
                        )}

                        <div className="auth-link-box">
                            <Link to="/login" className="link-secondary">
                                Voltar para login
                            </Link>
                        </div>

                        <div className="auth-link-box">
                            <Link to="/register" className="link-secondary">
                                Não tem conta? Criar conta aqui.
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

export default ForgotPassword;
