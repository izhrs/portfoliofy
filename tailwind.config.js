module.exports = {
    darkMode: "class",
    // Your project's files to scan for Tailwind classes
    content: ["./static/**/*.{html,py,js}", "./templates/**/*.{html,py,js}"],
    theme: {
        extend: {
            // Colors that match with UNFOLD["COLORS"] settings
            colors: {
                base: {
                    50: "rgb(var(--color-base-50))",
                    100: "rgb(var(--color-base-100))",
                    200: "rgb(var(--color-base-200))",
                    300: "rgb(var(--color-base-300))",
                    400: "rgb(var(--color-base-400))",
                    500: "rgb(var(--color-base-500))",
                    600: "rgb(var(--color-base-600))",
                    700: "rgb(var(--color-base-700))",
                    800: "rgb(var(--color-base-800))",
                    900: "rgb(var(--color-base-900))",
                    950: "rgb(var(--color-base-950))",
                },
                primary: {
                    50: "rgb(var(--color-primary-50))",
                    100: "rgb(var(--color-primary-100))",
                    200: "rgb(var(--color-primary-200))",
                    300: "rgb(var(--color-primary-300))",
                    400: "rgb(var(--color-primary-400))",
                    500: "rgb(var(--color-primary-500))",
                    600: "rgb(var(--color-primary-600))",
                    700: "rgb(var(--color-primary-700))",
                    800: "rgb(var(--color-primary-800))",
                    900: "rgb(var(--color-primary-900))",
                    950: "rgb(var(--color-primary-950))",
                },
                font: {
                    "subtle-light": "rgb(var(--color-font-subtle-light))",
                    "subtle-dark": "rgb(var(--color-font-subtle-dark))",
                    "default-light": "rgb(var(--color-font-default-light))",
                    "default-dark": "rgb(var(--color-font-default-dark))",
                    "important-light": "rgb(var(--color-font-important-light))",
                    "important-dark": "rgb(var(--color-font-important-dark))",
                },
            },
        },
    },
};
