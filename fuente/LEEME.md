# Código fuente de la app APM

- `apm_body.html`: contenido de la app (marcado y JavaScript). Aquí se edita la app.
- `build_apm.py`: genera `index.html` a partir de `apm_body.html`.
- `prea.js`: prerenderiza el contenido para que se lea sin JavaScript.

Pendiente: `build_apm.py` todavía toma partes del CSS de un fichero que no está en este repositorio. Hasta que se haga autocontenido, la publicación automática no está activa.

- **Mi camino** (módulo añadido en noviembre de 2026): integra el «Manual de entrada · Tu primer destino» de la APM (`Manual-de-entrada-APM.pdf`, en la raíz). Su contenido está en `apm_body.html`, en el bloque «MI CAMINO» (preguntas `SUST` y `PDQ`, listas `LISTAS`, guías `GUIAS`, fases `FASES`). Los datos marcados con `VER` están pendientes de verificar.
