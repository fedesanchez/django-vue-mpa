const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
	content: [
		"./dashboard/templates/**/*.html",
		"./static/src/js/**/*.{js,jsx,ts,tsx,vue}",
	],
	darkMode: "class",
	plugins: [require("@tailwindcss/forms")],
	theme: {
		extend: {
			fontFamily: {
				sans: ["Inter", ...defaultTheme.fontFamily.sans],
			},
			boxShadow: {
				bottom: "0 5px 6px -7px rgba(0, 0, 0, 0.6), 0 2px 4px -5px rgba(0, 0, 0, 0.06)",
			},
		},
	},
};
