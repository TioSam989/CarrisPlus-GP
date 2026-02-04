import React, { useState } from 'react';

const ConsultarPasse = () => {
    const [searchValue, setSearchValue] = useState('');
    const [showPass, setShowPass] = useState(false);

    // Mock pass data - replace with actual API call
    const passData = {
        status: 'VÁLIDO',
        validity: '11/2030',
        balance: '50 EUR',
        address: 'Rua de Lisboa 99, Lisboa',
        name: 'IAGO IAGUEIRA IAGAO'
    };

    const handleSearch = (e) => {
        e.preventDefault();
        if (searchValue) {
            setShowPass(true);
        }
    };

    return (
        <div className="max-w-6xl mx-auto p-6">
            <h1 className="text-4xl font-bold text-center mb-8">
                CONSULTE <span className="text-carris-yellow">AQUI</span> O SEU PASSE
            </h1>

            {/* Search Input */}
            <form onSubmit={handleSearch} className="mb-12">
                <input
                    type="text"
                    value={searchValue}
                    onChange={(e) => setSearchValue(e.target.value)}
                    placeholder="DIGITE AQUI O SEU EMAIL OU CONTRIBUINTE"
                    className="w-full px-6 py-4 bg-gray-200 border-none rounded-lg focus:outline-none focus:ring-2 focus:ring-carris-yellow text-gray-700 placeholder-gray-500"
                />
            </form>

            {/* Pass Display */}
            {showPass && (
                <div className="flex flex-col lg:flex-row gap-8 items-center lg:items-start">
                    {/* Pass Info */}
                    <div className="flex-1 space-y-4 text-lg">
                        <div>
                            <span className="font-bold">STATUS:</span>{' '}
                            <span className="font-bold text-green-600">{passData.status}</span>
                        </div>
                        <div>
                            <span className="font-bold">VALIDADE:</span>{' '}
                            <span>{passData.validity}</span>
                        </div>
                        <div>
                            <span className="font-bold">SALDO:</span>{' '}
                            <span>{passData.balance}</span>
                        </div>
                        <div>
                            <span className="font-bold">MORADA:</span>{' '}
                            <span>{passData.address}</span>
                        </div>
                        <div>
                            <span className="font-bold">NOME:</span>{' '}
                            <span>{passData.name}</span>
                        </div>
                    </div>

                    {/* Pass Card */}
                    <div className="flex-1 flex justify-center">
                        <div className="relative w-full max-w-md">
                            {/* Black curve decoration */}
                            <div className="absolute right-0 top-0 w-48 h-48 bg-black rounded-full transform translate-x-24 -translate-y-12"></div>

                            <div className="relative bg-carris-yellow rounded-2xl p-8 shadow-2xl">
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
                                            <div>{passData.validity}</div>
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
                                        {passData.name}
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
            )}
        </div>
    );
};

export default ConsultarPasse;
