function btn() {
    let theme = document.getElementById("theme-link");

    if (theme.getAttribute("href") === "/static/main/css/darkTheme.css") {
        theme.href = "/static/main/css/lightTheme.css";
    } else {
        theme.href = "/static/main/css/darkTheme.css";
    }
}