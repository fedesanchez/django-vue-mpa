import vue from "@vitejs/plugin-vue";
import dynaminImport from "vite-plugin-dynamic-import";
const { resolve } = require("path");

module.exports = {
	plugins: [vue(), dynaminImport()],
	root: resolve("./static/src"),
	base: "/static/",
	server: {
		host: "0.0.0.0",
		port: 5173,
		open: false,
		watch: {
			usePolling: true,
			disableGlobbing: false,
		},
	},
	resolve: {
		extensions: [".js", ".json", ".vue"],
		alias: {
			"@": resolve(__dirname, "./static/src/js"),
		},
	},
	build: {
		outDir: resolve("./static/dist"),
		assetsDir: "",
		manifest: true,
		emptyOutDir: true,
		target: "es2015",
		rollupOptions: {
			input: {
				main: resolve("./static/src/js/main.js"),
			},
			output: {
				chunkFileNames: "./static/src/js/[name].js?id=[chunkHash]",
			},
		},
	},
};
