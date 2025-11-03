# Episodio 05 — IA para limpiar y transformar datos

**E:** ¿Por qué usar IA en vez de solo pandas/SQL?
**I:** Para describir transformaciones en lenguaje natural y que te devuelva el código. Acelera cuando no recuerdas la sintaxis o el dataset es sucio.

**E:** ¿Patrón práctico?
**I:** Prompt -> propuesta de código (pandas/SQL) -> validador -> ejecución en sandbox -> resultado + diff de filas afectadas.

**E:** ¿Cómo evitas errores peligrosos?
**I:** Whitelist de operaciones, límites de tiempo y tamaño, y siempre review humano antes de aplicar en producción.

**E:** ¿Entrega para el oyente?
**I:** Script que recibe un CSV y una instrucción: “normaliza emails, corrige tildes, elimina duplicados y da un resumen de cambios”.
