const botonTema = document.getElementById("botonTema");
const body = document.body;

function toggleTheme() {
    body.classList.toggle("dark-mode");
    const modoOscuro = body.classList.contains("dark-mode");
    botonTema.textContent = modoOscuro ? "Modo día" : "Modo noche";
    localStorage.setItem("tema", modoOscuro ? "oscuro" : "claro");
}

if (botonTema) botonTema.addEventListener("click", toggleTheme);

window.addEventListener("DOMContentLoaded", () => {
    const temaGuardado = localStorage.getItem("tema");
    if (temaGuardado === "oscuro") {
        body.classList.add("dark-mode");
        if (botonTema) botonTema.textContent = "Modo día";
    } else {
        if (botonTema) botonTema.textContent = "Modo noche";
    }
});