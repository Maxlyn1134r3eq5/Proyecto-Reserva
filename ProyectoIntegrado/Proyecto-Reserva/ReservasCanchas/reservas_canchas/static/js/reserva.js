// reserva.js (Lógica para crear_reserva.html)

document.addEventListener('DOMContentLoaded', () => {
    // 1. Referencias a los elementos del DOM
    const canchaSelect = document.getElementById('cancha_select');
    const fechaInput = document.getElementById('fecha_input');
    const horaInicioSelect = document.getElementById('hora_inicio_select');
    const duracionSelect = document.getElementById('duracion_select');
    const costoTotalDisplay = document.getElementById('costoTotal');
    const cantidadJugadoresInput = document.getElementById('cantidad_jugadores_input');
    const jugadoresValorDisplay = document.getElementById('jugadores_valor'); // Para mostrar el valor del slider
    const btnGuardar = document.getElementById('btnGuardar');

    let precioPorHora = 0; // Almacena el precio de la cancha

    // --- FUNCIONES DE LÓGICA DE RESERVA ---

    /**
     * Simula la verificación de disponibilidad (Será reemplazada por FETCH al Backend).
     */
    function verificarDisponibilidad(canchaId, fecha) {
        // En el futuro: FETCH al Backend para obtener horarios NO reservados.
        console.log(`Verificando disponibilidad para Cancha ${canchaId} en ${fecha}`);
        
        // SIMULACIÓN DE HORARIOS DISPONIBLES:
        const horariosDisponibles = ['17:00', '18:30', '20:00', '21:30'];
        
        // Llenar el selector
        horaInicioSelect.innerHTML = '<option value="">Selecciona hora</option>';
        horariosDisponibles.forEach(hora => {
            const option = document.createElement('option');
            option.value = hora;
            option.textContent = hora;
            horaInicioSelect.appendChild(option);
        });

        horaInicioSelect.disabled = false;
    }

    /**
     * Calcula el costo total y habilita/deshabilita el botón de pago.
     */
    function actualizarCosto() {
        const duracion = parseFloat(duracionSelect.value);
        
        // Condición para habilitar el botón (validación de todos los campos)
        const esValido = precioPorHora > 0 && 
                         !isNaN(duracion) && 
                         horaInicioSelect.value && 
                         cantidadJugadoresInput.value >= cantidadJugadoresInput.min;

        if (!esValido) {
            costoTotalDisplay.textContent = '$0';
            btnGuardar.disabled = true;
            return;
        }

        const costo = precioPorHora * duracion;
        costoTotalDisplay.textContent = `$${costo.toLocaleString('es-CL')}`;
        btnGuardar.disabled = false;
    }
    
    // --- EVENT LISTENERS (MANEJO DE INTERACCIÓN) ---
    
    // A. Cuando la cancha cambia:
    canchaSelect.addEventListener('change', (e) => {
        const selectedOption = e.target.options[e.target.selectedIndex];
        precioPorHora = parseFloat(selectedOption.getAttribute('data-precio')) || 0;
        
        if (fechaInput.value && precioPorHora > 0) {
            verificarDisponibilidad(canchaSelect.value, fechaInput.value);
        } else {
            horaInicioSelect.disabled = true;
            horaInicioSelect.innerHTML = '<option value="">Selecciona cancha y fecha</option>';
        }
        actualizarCosto();
    });

    // B. Cuando la fecha cambia:
    fechaInput.addEventListener('change', (e) => {
        if (canchaSelect.value && e.target.value) {
            verificarDisponibilidad(canchaSelect.value, e.target.value);
        }
        actualizarCosto();
    });

    // C. Recalcular costo al cambiar duración u hora de inicio
    duracionSelect.addEventListener('change', actualizarCosto);
    horaInicioSelect.addEventListener('change', actualizarCosto);
    
    // D. SLIDER: Mostrar el valor del slider y recalcular costo
    cantidadJugadoresInput.addEventListener('input', () => {
        jugadoresValorDisplay.textContent = cantidadJugadoresInput.value;
        actualizarCosto();
    });
    
    // Inicializar el botón deshabilitado al cargar
    btnGuardar.disabled = true;
});

document.getElementById("fecha_input").addEventListener("change", cargarHoras);

async function cargarHoras() {
    const cancha = document.getElementById("cancha_select").value;
    const fecha = document.getElementById("fecha_input").value;

    if (!cancha || !fecha) return;

    let res = await fetch(`/reservas/horas_disponibles/?cancha=${cancha}&fecha=${fecha}`);
    let data = await res.json();

    let selectHoras = document.getElementById("hora_inicio_select");
    selectHoras.innerHTML = "";

    data.horas.forEach(h => {
        let option = document.createElement("option");
        option.value = h;
        option.textContent = h;
        selectHoras.appendChild(option);
    });

    selectHoras.disabled = false;
}
