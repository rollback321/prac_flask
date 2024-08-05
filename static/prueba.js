$(document).ready(function() {   
    $('.class_prueba').click(function() {
        $.ajax({
            url: '/get_data',  // Ruta en Flask para obtener datos
            type: 'POST',        // Método de la solicitud (GET, POST, etc.)
            contentType: 'application/json',
            data: JSON.stringify({
                'nombre': 'Juan',
                'edad': 30
            }),
            dataType: 'json',
            success: function(data) {
                // Manejar la respuesta exitosa
                console.log(data);
                // $('.class_prueba').text(data.message);  // Mostrar el mensaje en un elemento HTML
            },
            error: function(xhr, status, error) {
                // Manejar errores de la solicitud
                console.error('Error al obtener datos:', error);
            }
        });
    });
});
