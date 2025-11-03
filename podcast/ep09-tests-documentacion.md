# Episodio 09 — Genera tests y documentación automática con IA

**E:** ¿Qué genera bien y qué no?
**I:** Genera borradores de tests unitarios, docstrings y README. No esperes cobertura perfecta: sirve para acelerar y que tú ajustes.

**E:** ¿Flujo recomendado?
**I:** Detecto funciones sin tests, paso la firma y casos límite, pido tests parametrizados y reviso. Para docs, pido ejemplos concretos y tablas.

**E:** ¿Cómo mantener consistencia?
**I:** Pautas de estilo en el prompt y un linter/formatter en CI. Si el modelo se contradice, tengo reglas de validación que fallan el PR.
