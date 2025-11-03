# Episodio 03 — Asistente que entiende tu código (RAG sobre repos)

**E:** ¿Qué problema resuelve?
**I:** Encontrar y explicar partes de un repo grande: funciones, contratos, decisiones de diseño. En vez de buscar manualmente, preguntas en lenguaje natural.

**E:** ¿Cómo funciona a alto nivel?
**I:** Indexo el repo (chunks + embeddings) y hago búsqueda semántica. Paso los fragmentos relevantes como contexto a un modelo y lo instruyo para citar rutas de archivo.

**E:** ¿Primer MVP?
**I:** 1) Parseo archivos (excluyo binarios), 2) troceo por funciones/clases, 3) genero embeddings, 4) guardo en una BD vectorial (FAISS, Chroma), 5) API `/ask-code` que consulta y responde.

**E:** ¿Cómo evitas respuestas desfasadas?
**I:** Incluyo el commit SHA en el contexto y fuerzo al modelo a responder solo con lo que ve en los fragmentos. Si no está, que diga “no lo sé”.

**E:** ¿Mantenimiento?
**I:** Reindexo en cada merge a `main`. Y tengo tests que verifican que el asistente cita el archivo correcto y línea aproximada.
