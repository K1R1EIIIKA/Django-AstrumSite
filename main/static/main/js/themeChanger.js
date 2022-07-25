let activeTheme = localStorage.getItem("theme");
let theme = document.getElementById("theme-link");
const light = "/static/main/css/lightTheme.css";
const dark = "/static/main/css/darkTheme.css";

function btn() {
    if (theme.getAttribute("href") === dark) {
        theme.href = light;
        localStorage.setItem("theme", light);
    } else {
        theme.href = dark;
        localStorage.setItem("theme", dark);
    }
}

if (activeTheme === null) {
    theme.href = light;
} else {
    theme.href = activeTheme;
}