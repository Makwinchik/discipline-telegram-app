import type { Config } from 'tailwindcss';
export default { content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'], theme: { extend: { colors: { forge: { bg: '#05070d', card: '#0c111d', accent: '#8b5cf6' } } } }, plugins: [] } satisfies Config;
