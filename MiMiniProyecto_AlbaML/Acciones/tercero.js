document.addEventListener("DOMContentLoaded", function() {

  // Botón que redirige
  const botonRedirigir = document.getElementById("miBoton");
  if (botonRedirigir) {
    botonRedirigir.addEventListener("click", function() {
      location.href = "/Secundaria/Indice2.html";
    });
  }

  // Botón que muestra la banda
  const botonMostrar = document.getElementById("mostrarBtn");
  const banda = document.getElementById("banda");

  if (botonMostrar && banda) {
    botonMostrar.addEventListener("click", function() {
      banda.classList.add("mostrar");

      setTimeout(() => {
        banda.classList.remove("mostrar");
      }, 6000);
    });
  }

});

  // Botón que muestra la banda
  const botonMostrar2 = document.getElementById("mostrarBtn2");
  const banda2 = document.getElementById("banda2");

  if (botonMostrar2 && banda2) {
    botonMostrar2.addEventListener("click", function() {
      banda2.classList.add("mostrar2");

      setTimeout(() => {
        banda2.classList.remove("mostrar2");
      }, 3000);
    });
  }