document.addEventListener("DOMContentLoaded", (event) => {
  let form = document.getElementById("formTexto");
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    let texto = document.querySelector("#texto");
    let valor_texto = texto.value;
    if (valor_texto === "") {
      customAlert("Por favor, no olvide escribir el texto a traducir", 0);
      texto.focus();
      return;
    }

    /**
     * Seleccionar el lenguaje de destino, y verificar que no este deshabilitado es decir que no sea el mismo lenguaje de origen
     */
    let lenguajeDestino = document.querySelector("#lenguajeDestino");
    let valor_lenguajeDestino = lenguajeDestino.value;
    if (lenguajeDestino.options[lenguajeDestino.selectedIndex].disabled) {
      customAlert("El idioma seleccionado en destino está deshabilitado", 0);
      return;
    }

    const formData = new FormData(form);
    // Agregar lenguaje de destino al FormData
    formData.append("lenguajeDestino", valor_lenguajeDestino);
    try {
      const response = await axios({
        method: "post",
        url: "/traducir-contenido/",
        data: formData,
        headers: {
          "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
          "Content-Type": "application/json",
        },
      });

      const { data, status } = response;
      if (status == 200) {
        document.querySelector("#resultTranslatedText").textContent =
          response.data.data;
        console.log("El texto traducido es: ", data);
      } else {
        customAlert("No hay traducciones disponibles", 0);
        console.log("No hay traducciones disponibles");
      }
    } catch (error) {
      console.log("Error al traducir el texto", error);
    }
  });
});

/**
 * Verificar si el textarea no esta vacio, caso contario limpiar el textarea resultado de la traduccion
 */
let textarea = document.querySelector("#texto");
textarea.addEventListener("blur", function (event) {
  if (textarea.value === "") {
    document.querySelector("#resultTranslatedText").value = "";
  }
  // console.log("El usuario hizo clic fuera del textarea.");
});

function actualizarSegundoSelect(idiomaSeleccionado) {
  var segundoSelect = document.getElementById("lenguajeDestino");
  var opciones = segundoSelect.options;

  for (var i = 0; i < opciones.length; i++) {
    if (opciones[i].value === idiomaSeleccionado) {
      opciones[i].disabled = true;
    } else {
      opciones[i].disabled = false;
    }
  }
}

function customAlert(msj, tipo_msj) {
  const divExistente = document.querySelector(".alert");
  if (divExistente) {
    divExistente.remove();
  }

  const divRespuesta = document.createElement("div");
  divRespuesta.innerHTML = `
    <div class="alert ${
      tipo_msj == 1 ? "alert-success" : "alert-warning"
    }  alert-dismissible text-center" role="alert" style="font-size: 17px;">
      ${msj}
    </div>
  `;

  setTimeout(function () {
    divRespuesta.innerHTML = "";
  }, 5000);

  const container = document.querySelector(".first_row");
  container.insertAdjacentElement("beforeend", divRespuesta);
}
