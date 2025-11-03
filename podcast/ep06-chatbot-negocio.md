# Episodio 06 — Chatbot que sabe de tu negocio (RAG aplicado)

**E:** ¿Qué diferencia a un chatbot “listo” de uno básico?
**I:** El listo tiene acceso a tus documentos, FAQs y políticas. No inventa: busca, cita y responde con base en tus datos.

**E:** ¿Stack mínimo?
**I:** Ingesta de documentos, embeddings, base vectorial, y un servidor que hace retrieve+generate. Si necesitas orquestación, LangChain/LlamaIndex.

**E:** ¿Cómo manejas actualizaciones de contenido?
**I:** Reingesto incremental y versionado. Si cambia una política, reindexo ese documento y agrego fecha en la cita.

**E:** ¿Métrica clave?
**I:** Tasa de “respuesta con cita válida”. Si baja, hay que mejorar el retriever o los prompts.
