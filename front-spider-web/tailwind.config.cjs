/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',/* Prefixo usado nas classes do tailwind */
  important: false,/* Remove o importante do tailwind, evita problemas futuros de ter um site preso à ele */
  content: [
    "./index.html",
    "./src/components/**/*.vue",
    "./src/App.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
