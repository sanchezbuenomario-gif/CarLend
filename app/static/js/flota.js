// --- LÓGICA DEL MODAL (VER DETALLES Y RESERVAR) ---

function abrirDetalles(marca, modelo, precio, imagen, categoria, plazas) {
    // Guardamos los datos en el objeto global para el formulario
    cocheSeleccionado = {
        marca: marca,
        modelo: modelo,
        precio: precio,
        imagen: imagen
    };

    // Rellenamos el Modal con los datos recibidos por parámetros
    document.getElementById('detalleTitulo').innerText = marca + " " + modelo;
    document.getElementById('detCat').innerText = categoria.toUpperCase();
    document.getElementById('detPlazas').innerText = plazas;
    document.getElementById('detCiudad').innerText = "Disponible en Sede"; 
    document.getElementById('detPrecio').innerText = precio + "€ / día";
    
    // La imagen ya viene como URL del HTML
    document.getElementById('detalleImagen').style.backgroundImage = "url('" + imagen + "')";

    // Abrimos el modal
    const modal = document.getElementById('modalCarLend');
    modal.style.display = "flex";
    
    // Forzamos que se vea la vista de detalles y no el formulario
    document.getElementById('vistaDetalles').style.display = "block";
    document.getElementById('vistaFormulario').style.display = "none";
}

function cerrarModal() {
    document.getElementById('modalCarLend').style.display = "none";
}

function mostrarFormulario() {
    document.getElementById('vistaDetalles').style.display = "none";
    document.getElementById('vistaFormulario').style.display = "block";
    document.getElementById('reservaCocheInfo').innerText = "Vehículo seleccionado: " + cocheSeleccionado.marca + " " + cocheSeleccionado.modelo;
}

function volverADetalles() {
    document.getElementById('vistaDetalles').style.display = "block";
    document.getElementById('vistaFormulario').style.display = "none";
}

// Cerrar al hacer clic fuera
window.onclick = function(event) {
    const modal = document.getElementById('modalCarLend');
    if (event.target == modal) {
        cerrarModal();
    }
}