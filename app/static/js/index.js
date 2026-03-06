const navbar = document.getElementById("navbar");
const body = document.body;
const botonTema = document.getElementById("botonTema");
const menuHamburguesa = document.getElementById("menuHamburguesa");
const navLinks = document.querySelector(".nav-links");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 50);
});

if (localStorage.getItem("tema") === "oscuro") {
    body.classList.add("dark-mode");
    if (botonTema) botonTema.textContent = "Modo Día";
}

if (botonTema) {
    botonTema.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        botonTema.textContent = body.classList.contains("dark-mode") ? "Modo Día" : "Modo Noche";
        localStorage.setItem("tema", body.classList.contains("dark-mode") ? "oscuro" : "claro");
    });
}

if (menuHamburguesa && navLinks) {
    menuHamburguesa.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });
}

const pista = document.getElementById("pistaCarrusel");
const prevBtn = document.getElementById("carruselPrev");
const nextBtn = document.getElementById("carruselNext");

if (pista) {
    let tarjetas = Array.from(pista.querySelectorAll(".tarjeta-coche"));

    tarjetas.forEach(t => pista.appendChild(t.cloneNode(true)));
    tarjetas = Array.from(pista.querySelectorAll(".tarjeta-coche"));

    const gap = 20;
    const tarjetaWidth = tarjetas[0].offsetWidth + gap;
    pista.scrollLeft = 0;

    function scrollInfinite(direccion) {
        pista.scrollBy({ left: tarjetaWidth * direccion, behavior: "smooth" });
        setTimeout(() => {
            if (pista.scrollLeft >= pista.scrollWidth / 2) {
                pista.scrollLeft -= pista.scrollWidth / 2;
            } else if (pista.scrollLeft <= 0) {
                pista.scrollLeft += pista.scrollWidth / 2;
            }
        }, 300);
    }

    if (prevBtn) prevBtn.addEventListener("click", () => scrollInfinite(-1));
    if (nextBtn) nextBtn.addEventListener("click", () => scrollInfinite(1));

    let isDown = false, startX, scrollLeft;

    pista.addEventListener("mousedown", e => {
        isDown = true;
        pista.classList.add("is-dragging");
        startX = e.pageX - pista.offsetLeft;
        scrollLeft = pista.scrollLeft;
    });

    pista.addEventListener("mouseleave", () => { isDown = false; pista.classList.remove("is-dragging"); });
    pista.addEventListener("mouseup", () => { isDown = false; pista.classList.remove("is-dragging"); });

    pista.addEventListener("mousemove", e => {
        if (!isDown) return;
        const x = e.pageX - pista.offsetLeft;
        const walk = (x - startX) * 1.4;
        pista.scrollLeft = scrollLeft - walk;
        if (pista.scrollLeft >= pista.scrollWidth / 2) pista.scrollLeft -= pista.scrollWidth / 2;
        else if (pista.scrollLeft <= 0) pista.scrollLeft += pista.scrollWidth / 2;
    });

    pista.addEventListener("touchstart", e => {
        isDown = true;
        startX = e.touches[0].pageX - pista.offsetLeft;
        scrollLeft = pista.scrollLeft;
    });

    pista.addEventListener("touchend", () => isDown = false);

    pista.addEventListener("touchmove", e => {
        if (!isDown) return;
        const x = e.touches[0].pageX - pista.offsetLeft;
        const walk = (x - startX) * 1.4;
        pista.scrollLeft = scrollLeft - walk;
        if (pista.scrollLeft >= pista.scrollWidth / 2) pista.scrollLeft -= pista.scrollWidth / 2;
        else if (pista.scrollLeft <= 0) pista.scrollLeft += pista.scrollWidth / 2;
    });

    tarjetas.forEach(tarjeta => {
        tarjeta.addEventListener('mousemove', e => {
            const rect = tarjeta.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * 10;
            const rotateY = ((x - centerX) / centerX) * 10;
            tarjeta.style.transform = `perspective(1200px) rotateX(${-rotateX}deg) rotateY(${rotateY}deg) scale(1.05) translateY(-10px)`;
        });
        tarjeta.addEventListener('mouseleave', () => {
            tarjeta.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) scale(1) translateY(0px)';
        });
    });

    window.addEventListener("resize", () => {
        tarjetas = Array.from(pista.querySelectorAll(".tarjeta-coche"));
    });
}