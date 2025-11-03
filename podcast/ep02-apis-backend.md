# Episodio 02 — Usando APIs de IA desde tu backend

**E:** ¿Cuándo tiene sentido llamar a una API de IA desde el backend?
**I:** Cuando necesitas transformar texto, clasificar, generar resúmenes o asistir al usuario sin exponer la API key en el frontend. El backend controla coste, rate limiting y seguridad.

**E:** ¿Patrones de diseño?
**I:** Endpoint interno `/ai/*` que valida input, añade contexto y delega a la API. Cacheo respuestas frecuentes y registro métricas (tokens, latencia, tasa de error).

**E:** ¿Cómo evitar que la IA invente cosas?
**I:** Restringe el output: formatos fijos (JSON schema), instrucciones claras y validación server-side. Si el modelo se inventa datos, responde con `null` y loguea.

**E:** ¿Ejemplo rápido?
**I:** `POST /ai/summarize` recibe texto y devuelve bullets. En el servidor, seteo `max_tokens`, temperatura baja y un `system` que establezca estilo conciso.

**E:** ¿Qué hay del coste?
**I:** Añade un middleware que estime coste por request y define límites por usuario/plan. Y ten reintentos con backoff para errores 429/5xx.

**E:** ¿Observabilidad?
**I:** Logueo: prompt, tamaño, respuesta, latencia, coste, y un ID de correlación. Y creo dashboards para detectar desvíos.
