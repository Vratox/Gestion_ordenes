const guardarOrden = document.getElementById('crear_orden');

// 3. Agregar el oyente de click al botón de guardar UNA SOLA VEZ
guardarOrden.addEventListener('click', () => {
    console.log('El botón fue clickeado!');
    const formData = new FormData(document.getElementById('orden_cliente'));
    const data = Object.fromEntries(formData.entries());
    console.log('Datos del formulario:', data);

    // Asegúrate de que tu función getCookie esté definida
    fetch(`/ordenes/`, {
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
        alert('Orden guardado exitosamente!');
        
        // Opcional: Limpiar el formulario después del éxito
        document.getElementById('orden_cliente').reset();
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

var table = new Tabulator("#table_orden", {
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
    ajaxURL: '/ordenes/tableJson/', // URL de la API
    ajaxConfig: "GET", // Método HTTP
    ajaxResponse:function(url, params, response){
        console.log("Datos recibidos de la API: ", response);
        return response.data;
    },
    layout:"fitColumns",
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
            title:"cliente", field:"cliente", width:80,        
        },
        
        {
            title:"Titulo", field:"titulo", width:95, 
        },

        {
            title: "Estado", field: "estado", hozAlign: "center", width: 350,
        },
    ],
});