// 3. El JavaScript para controlar el modal
document.addEventListener('DOMContentLoaded', (event) => {
var modal = document.getElementById("errorModal");
var closeButton = document.querySelector(".close-button");

// Muestra el modal si existe un mensaje de error
if (modal && modal.style.display === "block") {
    modal.style.display = "block";
}

// Cierra el modal al hacer clic en el botón de cerrar
closeButton.onclick = function() {
    modal.style.display = "none";
}

// Cierra el modal al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
});

document.addEventListener('DOMContentLoaded', (event) => {
var modalUserNew = document.getElementById("userNewModal");
var closeButton = document.querySelector(".btn-close");

// Muestra el modal si existe un mensaje de error
if (modalUserNew && modalUserNew.style.display === "block") {
    modalUserNew.style.display = "block";
}

// Cierra el modal al hacer clic en el botón de cerrar
closeButton.onclick = function() {
    modalUserNew.style.display = "none";
}

// Cierra el modal al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target == modalUserNew) {
        modalUserNew.style.display = "none";
    }
}
});


const btnGuardar = document.getElementById('btnSavePassword');

btnGuardar.addEventListener('click', () => {
    console.log('El botón fue clickeado!');
    const password = document.getElementById('passwordUser').value;
    const passwordConfirm = document.getElementById('passwordRepeat').value;

    if (password !== passwordConfirm) {
        alert('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.');
        return;
    }

    const formData = new FormData(document.getElementById('formPassword'));    
    const data = Object.fromEntries(formData.entries());

    // Asegúrate de que tu función getCookie esté definida
    fetch(`/repeatPassword/`, {
        method: "POST", 
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json",
        }, 
        body: JSON.stringify(data)
    })
    .then(response => response.json().then(data => ({
        ok: response.ok,
        status: response.status,
        data
    })))
    .then(({ ok, status, data }) => {
        if (ok && data.success) {
        console.log("Cliente guardado:", data);
        alert(data.message);

        modalBootstrapInstance.hide();
        document.getElementById("formPassword").reset();
        }   else {
        // Error controlado desde el backend
        console.warn("Error controlado:", data);
        mostrarErroresEnPlantilla(data);
        }
    })
    .catch(error => {
        console.error("Error inesperado:", error);
        lert("Ocurrió un error inesperado. Por favor, inténtalo de nuevo.");
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}