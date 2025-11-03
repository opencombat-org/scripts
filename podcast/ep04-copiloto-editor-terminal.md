# Episodio 04 — Tu propio copiloto para terminal o VSCode

**E:** ¿Qué es lo mínimo viable?
**I:** Un comando `ai` que lee stdin y devuelve salida. Lo enlazo a atajos en VSCode y a funciones de shell. No hace falta construir una extensión desde cero.

**E:** ¿Casos de uso reales?
**I:** Explicar errores, reescribir funciones, generar snippets y crear bash one-liners. También plantillas de tests y migraciones.

**E:** ¿Cómo controlas el estilo del código generado?
**I:** Prompts con reglas: versión de lenguaje, linter, convenciones y límites (no tocar I/O, mantener firma). Y paso ejemplos de antes/después.

**E:** ¿Privacidad y secretos?
**I:** Filtrado previo: quito `.env`, claves y rutas sensibles. Y en VSCode, desactivo enviar telemetría del proyecto si es confidencial.
