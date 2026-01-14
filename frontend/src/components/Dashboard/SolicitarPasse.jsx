import React, { useState } from 'react';

const SolicitarPasse = () => {
    const [formData, setFormData] = useState({
        fullName: '',
        nif: '',
        phone: '',
        address: '',
        nationality: '',
        emergencyContact: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // TODO: Implement pass request submission
        console.log('Pass request:', formData);
    };

    return (
        <div className="flex flex-col lg:flex-row gap-8 p-6 max-w-7xl mx-auto">
            {/* Form Section */}
            <div className="flex-1 bg-white rounded-lg p-6">
                <h2 className="text-2xl font-bold mb-2">
                    Preencha os campos abaixo para{' '}
                    <span className="text-carris-yellow">solicitar o seu Passe</span>.
                </h2>

                <form onSubmit={handleSubmit} className="space-y-4 mt-6">
                    <div>
                        <input
                            type="text"
                            name="fullName"
                            value={formData.fullName}
                            onChange={handleChange}
                            placeholder="Insira seu nome completo"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="text"
                            name="nif"
                            value={formData.nif}
                            onChange={handleChange}
                            placeholder="Insira seu NIF"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="tel"
                            name="phone"
                            value={formData.phone}
                            onChange={handleChange}
                            placeholder="Insira seu telemóvel"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="text"
                            name="address"
                            value={formData.address}
                            onChange={handleChange}
                            placeholder="Insira seu endereço"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="text"
                            name="nationality"
                            value={formData.nationality}
                            onChange={handleChange}
                            placeholder="Insira sua nacionalidade"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <div>
                        <input
                            type="text"
                            name="emergencyContact"
                            value={formData.emergencyContact}
                            onChange={handleChange}
                            placeholder="Insira um contato de emergência"
                            className="w-full px-4 py-3 bg-gray-100 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow"
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        className="w-full bg-carris-yellow text-black font-bold py-4 rounded-lg hover:bg-yellow-500 transition-colors"
                    >
                        🎫 SOLICITAR PASSE
                    </button>
                </form>
            </div>

            {/* Pass Preview Card */}
            <div className="flex-1 flex items-start justify-center lg:sticky lg:top-6">
                <div className="w-full max-w-md">
                    <div className="bg-carris-yellow rounded-2xl p-8 shadow-2xl">
                        {/* Card Header */}
                        <div className="flex justify-between items-start mb-6">
                            <div className="text-sm">
                                <div className="font-mono">000 000000000000</div>
                            </div>
                        </div>

                        {/* Photo and Info Section */}
                        <div className="flex gap-6 mb-6">
                            {/* Photo */}
                            <div className="w-24 h-24 bg-white rounded-lg flex items-center justify-center">
                                <svg className="w-16 h-16 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                                    <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                                </svg>
                            </div>

                            {/* Card Info */}
                            <div className="flex-1 text-xs space-y-1">
                                <div>
                                    <div className="font-bold">EMISSÃO</div>
                                    <div>11/2025</div>
                                </div>
                                <div>
                                    <div className="font-bold">VALIDADE</div>
                                    <div>11/2030</div>
                                </div>
                            </div>
                        </div>

                        {/* Pass Description */}
                        <div className="text-xs mb-6 leading-relaxed">
                            <p className="font-bold">
                                Cartão pessoal e<br />
                                intransmissível de validação<br />
                                obrigatória no início de cada<br />
                                viagem (inclusive títulos<br />
                                gratuitos)
                            </p>
                            <p className="mt-2">
                                A quem o encontrar pede-se o<br />
                                favor de o entregar num posto<br />
                                de atendimento.
                            </p>
                        </div>

                        {/* User Info */}
                        <div className="border-t border-black pt-4">
                            <div className="font-bold text-sm mb-2">
                                {formData.fullName || 'NOME COMPLETO'}
                            </div>

                            {/* Transport Icons */}
                            <div className="flex gap-3 mb-4">
                                <div className="w-8 h-8 bg-black rounded"></div>
                                <div className="w-8 h-8 bg-black rounded"></div>
                                <div className="w-8 h-8 bg-black rounded"></div>
                                <div className="w-8 h-8 bg-black rounded"></div>
                            </div>

                            {/* Serial Number */}
                            <div className="font-mono text-xs">
                                000000000000AA0000
                            </div>
                        </div>

                        {/* Footer */}
                        <div className="mt-4 text-[10px] text-center">
                            <div className="font-bold">transportes</div>
                            <div className="flex justify-center items-center gap-1">
                                <span>metropolitanos</span>
                                <span className="text-xs">de</span>
                                <span className="flex gap-1">
                                    <span className="text-yellow-600">●</span>
                                    <span className="text-green-600">●</span>
                                    <span className="text-blue-600">●</span>
                                </span>
                                <span>lisboa</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SolicitarPasse;
