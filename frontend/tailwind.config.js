/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'carris-yellow': '#FFD700',
        'carris-black': '#1A1A1A',
        'carris-blue': '#00BFFF',
      },
    },
  },
  plugins: [],
}
