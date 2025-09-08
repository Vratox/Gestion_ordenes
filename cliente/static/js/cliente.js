// 1. Obtener la instancia del modal y crear el objeto de Bootstrap UNA SOLA VEZ
const modalElement = document.getElementById('modalClienteCrear');
const modalBootstrapInstance = new bootstrap.Modal(modalElement);

// 2. Obtener el botón de guardar UNA SOLA VEZ
const guardarBtn = document.getElementById('guardar_cliente');

// 3. Agregar el oyente de click al botón de guardar UNA SOLA VEZ
guardarBtn.addEventListener('click', () => {
    console.log('El botón fue clickeado!');
    const formData = new FormData(document.getElementById('crear-cliente-form'));
    const data = Object.fromEntries(formData.entries());

    // Asegúrate de que tu función getCookie esté definida
    fetch(`/cliente/`, {
        method: "POST", 
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json",
        }, 
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        return response.json().then(errorData => {
            throw { status: response.status, data: errorData };
        });
    })
    .then(data => {
        console.log('Cliente guardado:', data);
        alert('Cliente guardado exitosamente!');
        
        // 4. Usar la instancia de Bootstrap para cerrar el modal
        modalBootstrapInstance.hide();
        
        // Opcional: Limpiar el formulario después del éxito
        document.getElementById('crear-cliente-form').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        if (error.status === 400 && error.data) {
            mostrarErroresEnPlantilla(error.data);
        } else {
            alert('Ocurrió un error inesperado. Por favor, inténtalo de nuevo.');
        }
    });
});

function mostrarErroresEnPlantilla(errors) {
    // Primero, limpia los errores anteriores
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Itera sobre los errores y los muestra en el lugar correcto
    for (const field in errors) {
        // Asume que los IDs de los elementos de error son 'error-' + nombre del campo
        const errorElement = document.getElementById(`error-${field}`);
        if (errorElement) {
            // Unir los mensajes de error si hay varios para un campo
            errorElement.textContent = errors[field].join(', ');
        }
    }
    setTimeout(() => {
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
    }, 3000); // 5000 milisegundos = 5 segundos
}

// Helper function to get CSRF token from cookies
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

var table = new Tabulator("#table_cliente", {
    locale: true,
    langs: {
        es: {
        data: {
            loading: "Cargando Ordenes de trabajo...",
            error: "Error al cargar los datos",
        },
        groups: {
            item: "ítem",
            items: "ítems",
        },
        pagination: {
            page_size: "Tamaño de página",
            page_title: "Mostrar página",
            first: "Primera",
            first_title: "Primera página",
            last: "Última",
            last_title: "Última página",
            prev: "<",
            prev_title: "Página anterior",
            next: ">",
            next_title: "Página siguiente",
            all: "Todo",
        },
        headerFilters: {
            default: "filtrar columna...",
            columns: {},
        },
        },
    },

    locale:"es",
    ajaxURL: '/cliente/ClienteJson/', // URL de la API
    ajaxConfig: "GET", // Método HTTP
    ajaxResponse:function(url, params, response){
        console.log("Datos recibidos de la API: ", response);
        return response.data;
    },
    layout:"fitColumns",  
    theme:"bootstrap5",  
    responsiveLayout:"hide",
    sortMode: "remote",
    addRowPos:"top",
    history:true,
    pagination: "remote",
    paginationSize:5,
    paginationSizeSelector: [10, 25, 50, 100],
    initialSort:[ {column:"id", dir:"asc"} ],
    columnDefaults:{ tooltip:true },
    columns:[
        {
            title:"ID", field:"id", width:80,        
        },
        
        {
            title:"Nombre", field:"nombre", width:95, 
        },

        {
            title: "Correo", field: "email", hozAlign: "center", width: 350,
        },
    ],
});