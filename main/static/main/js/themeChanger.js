let activeTheme = localStorage.getItem("theme")
let theme = document.getElementById("theme-link");

function btn() {
    if (theme.getAttribute("href") === "/static/main/css/darkTheme.css") {
        theme.href = "/static/main/css/lightTheme.css";
        localStorage.setItem("theme", "/static/main/css/lightTheme.css")
    } else {
        theme.href = "/static/main/css/darkTheme.css";
        localStorage.setItem("theme", "/static/main/css/darkTheme.css")
    }
}

if (activeTheme === null) {
    theme.href = "/static/main/css/lightTheme.css";
} else {
    theme.href = activeTheme
}