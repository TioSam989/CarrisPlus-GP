/**
 * Dashboard Component
 * Main page after login
 */
import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { logoutUser } from '../store/authSlice';
import SolicitarPasse from './Dashboard/SolicitarPasse';
import ConsultarPasse from './Dashboard/ConsultarPasse';
import Configuracoes from './Dashboard/Configuracoes';

const Dashboard = () => {
    const { user } = useSelector((state) => state.auth);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [activeTab, setActiveTab] = useState('solicitar');

    const handleLogout = async () => {
        await dispatch(logoutUser());
        navigate('/login');
    };

    const tabs = [
        { id: 'solicitar', label: 'Solicitar Passe' },
        { id: 'consultar', label: 'Consultar Passe' },
        { id: 'configuracoes', label: 'Configurações' }
    ];

    return (
        <div className="min-h-screen bg-white">
            {/* Header */}
            <header className="bg-carris-yellow py-4 px-6 shadow-md">
                <div className="max-w-7xl mx-auto flex justify-between items-center">
                    <h1 className="text-3xl font-bold">
                        carris <span className="inline-flex items-center justify-center w-8 h-8 bg-black text-white rounded-full text-sm">id</span>
                    </h1>
                    <div className="flex items-center gap-4">
                        <div className="text-right">
                            <div className="font-bold">Olá!</div>
                            <div className="text-sm">{user?.full_name?.split(' ')[0]?.toUpperCase()}</div>
                        </div>
                        <button
                            onClick={handleLogout}
                            className="w-10 h-10 bg-black rounded-full flex items-center justify-center hover:bg-gray-800 transition-colors"
                            title="Sair"
                        >
                            <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                                <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                            </svg>
                        </button>
                    </div>
                </div>
            </header>

            {/* Navigation Tabs */}
            <nav className="bg-white border-b border-gray-200 py-4 px-6">
                <div className="max-w-7xl mx-auto flex gap-4 justify-center">
                    {tabs.map((tab) => (
                        <button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`px-8 py-3 rounded-full font-semibold transition-all ${
                                activeTab === tab.id
                                    ? 'bg-carris-black text-carris-yellow'
                                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                            }`}
                        >
                            {tab.label}
                        </button>
                    ))}
                </div>
            </nav>

            {/* Main Content */}
            <main className="py-8">
                {activeTab === 'solicitar' && <SolicitarPasse />}
                {activeTab === 'consultar' && <ConsultarPasse />}
                {activeTab === 'configuracoes' && <Configuracoes />}
            </main>
        </div>
    );
};

export default Dashboard;
