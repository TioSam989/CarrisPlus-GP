/**
 * Dashboard Component
 * Main page after login
 */
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { logoutUser } from '../store/authSlice';
import './Dashboard.css';

const Dashboard = () => {
    const { user } = useSelector((state) => state.auth);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleLogout = async () => {
        await dispatch(logoutUser());
        navigate('/login');
    };

    return (
        <div className="dashboard-container">
            <header className="dashboard-header">
                <h1>CarrisPlus</h1>
                <button onClick={handleLogout} className="btn-logout">
                    Sair
                </button>
            </header>

            <main className="dashboard-main">
                <div className="welcome-card">
                    <h2>Bem-vindo, {user?.full_name}!</h2>
                    <p className="user-email">{user?.email}</p>
                    <p className="user-nif">NIF: {user?.nif}</p>
                    {user?.is_admin && (
                        <span className="admin-badge">Administrador</span>
                    )}
                </div>

                <div className="dashboard-cards">
                    <div className="dashboard-card">
                        <h3>Submeter Documento</h3>
                        <p>Envie os seus documentos para validação automática</p>
                        <button className="btn-card" disabled>
                            Em breve
                        </button>
                    </div>

                    <div className="dashboard-card">
                        <h3>Criar Passe</h3>
                        <p>Solicite um novo passe Carris</p>
                        <button className="btn-card" disabled>
                            Em breve
                        </button>
                    </div>

                    <div className="dashboard-card">
                        <h3>Meus Passes</h3>
                        <p>Consulte os seus passes ativos</p>
                        <button className="btn-card" disabled>
                            Em breve
                        </button>
                    </div>

                    <div className="dashboard-card">
                        <h3>Histórico</h3>
                        <p>Veja o histórico dos seus documentos</p>
                        <button className="btn-card" disabled>
                            Em breve
                        </button>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default Dashboard;
