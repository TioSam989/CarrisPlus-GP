import React, { useState } from 'react';

const Configuracoes = () => {
    const [passwords, setPasswords] = useState({
        newPassword: '',
        confirmPassword: ''
    });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleChange = (e) => {
        setPasswords({
            ...passwords,
            [e.target.name]: e.target.value
        });
        setError('');
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (passwords.newPassword !== passwords.confirmPassword) {
            setError('As senhas não coincidem');
            return;
        }

        if (passwords.newPassword.length < 8) {
            setError('A senha deve ter pelo menos 8 caracteres');
            return;
        }

        // TODO: Implement password change API call
        setSuccess('Senha alterada com sucesso!');
        setPasswords({ newPassword: '', confirmPassword: '' });
    };

    return (
        <div className="max-w-2xl mx-auto p-6">
            <div className="bg-carris-yellow rounded-2xl p-8 shadow-lg">
                <h1 className="text-4xl font-bold text-center mb-8">CONFIGURAÇÕES</h1>

                {error && (
                    <div className="mb-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
                        {error}
                    </div>
                )}

                {success && (
                    <div className="mb-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded-lg">
                        {success}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="space-y-6">
                    <div>
                        <input
                            type="password"
                            name="newPassword"
                            value={passwords.newPassword}
                            onChange={handleChange}
                            placeholder="Nova senha"
                            className="w-full px-6 py-4 bg-white border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="password"
                            name="confirmPassword"
                            value={passwords.confirmPassword}
                            onChange={handleChange}
                            placeholder="Digite novamente a nova senha"
                            className="w-full px-6 py-4 bg-white border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-black"
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        className="w-full bg-black text-white font-bold py-4 rounded-lg hover:bg-gray-800 transition-colors"
                    >
                        Salvar
                    </button>
                </form>

                {/* Progress Bar (decorative) */}
                <div className="mt-8">
                    <div className="h-2 bg-black rounded-full"></div>
                </div>

                {/* Support Button */}
                <button className="w-full mt-6 bg-black text-white font-bold py-4 rounded-lg hover:bg-gray-800 transition-colors">
                    Solicitar Suporte
                </button>
            </div>
        </div>
    );
};

export default Configuracoes;
