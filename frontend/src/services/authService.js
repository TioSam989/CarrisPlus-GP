/**
 * Authentication Service
 * Handles login, register, and logout operations
 */
import api from './api';

const authService = {
    /**
     * Register a new user
     * @param {Object} userData - User registration data
     * @returns {Promise} Response data with token and user
     */
    register: async (userData) => {
        try {
            const response = await api.post('/api/auth/register', userData);

            // Store token and user data
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
            }

            return response.data;
        } catch (error) {
            throw error.response?.data || { error: 'Registration failed' };
        }
    },

    /**
     * Login user
     * @param {string} email - User email
     * @param {string} password - User password
     * @returns {Promise} Response data with token and user
     */
    login: async (email, password) => {
        try {
            const response = await api.post('/api/auth/login', {
                email,
                password
            });

            // Store token and user data
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
                localStorage.setItem('user', JSON.stringify(response.data.user));
            }

            return response.data;
        } catch (error) {
            throw error.response?.data || { error: 'Login failed' };
        }
    },

    /**
     * Logout user
     * @returns {Promise} Response data
     */
    logout: async () => {
        try {
            await api.post('/api/auth/logout');
        } catch (error) {
            console.error('Logout error:', error);
        } finally {
            // Clear local storage
            localStorage.removeItem('token');
            localStorage.removeItem('user');
        }
    },

    /**
     * Get current user from API
     * @returns {Promise} User data
     */
    getCurrentUser: async () => {
        try {
            const response = await api.get('/api/auth/me');
            return response.data.user;
        } catch (error) {
            throw error.response?.data || { error: 'Failed to get user' };
        }
    },

    /**
     * Check if user is logged in
     * @returns {boolean} True if logged in
     */
    isLoggedIn: () => {
        return !!localStorage.getItem('token');
    },

    /**
     * Get user from local storage
     * @returns {Object|null} User object or null
     */
    getUser: () => {
        const userStr = localStorage.getItem('user');
        return userStr ? JSON.parse(userStr) : null;
    },

    /**
     * Get token from local storage
     * @returns {string|null} Token or null
     */
    getToken: () => {
        return localStorage.getItem('token');
    }
};

export default authService;
