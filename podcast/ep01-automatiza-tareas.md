# Episodio 01 — Automatiza tus tareas con IA (sin complicarte la vida)

Formato: Entrevista breve con preguntas del entrevistador (E) y respuestas del invitado (I).

---

## 1) Arranque y contexto
**E:** Para un programador con poco tiempo, ¿qué problema real le soluciona la IA hoy mismo?
**I:** Me ahorra tareas repetitivas: redactar commits decentes, preparar README, generar esqueletos de tests, y resumir logs o PRs largos. No es magia, es productividad: le pido cosas concretas y me devuelve borradores útiles que yo reviso.

**E:** ¿Qué necesitas instalado para empezar en 10 minutos?
**I:** Un entorno Python o Node, una API key del proveedor que elijas (OpenAI, etc.), y un script CLI. Opcional: una extensión en VSCode tipo “copilot-like”.

---

## 2) Casos rápidos que uso a diario
**E:** Dame tres automatizaciones de 5 minutos.
**I:** 
1) Generar mensajes de commit a partir de `git diff`.
2) Resumir un archivo de log para detectar errores.
3) Escribir un primer borrador de changelog a partir de PRs cerrados.

**E:** ¿Cómo pides exactamente esos resultados?
**I:** Con prompts muy concretos: le doy el contexto (diff, log, lista de PRs) y le digo el formato de salida (bullet points, JSON, etc.). Cuanto más específico, mejor.

---

## 3) Ejemplo paso a paso (commit message desde git diff)
**E:** Explícanos el flujo.
**I:** 
1) Hago `git diff --staged` y capturo la salida.
2) Envío el diff al modelo con un prompt del tipo: “Resume cambios y propone un mensaje de commit en estilo convencional.”
3) Recibo 1–2 propuestas, elijo y edito.

**E:** ¿Riesgos o límites?
**I:** No le doy secretos. Si el diff es grande, resumo por partes. Y siempre reviso: la IA puede sonar convincente y estar equivocada.

---

## 4) Herramientas y snippets 
**E:** ¿Qué librerías te funcionan?
**I:** Para Node, `openai` u otras SDKs; para Python, `openai` y `requests`. Para flujos, `LangChain` si necesito orquestación, pero empiezo simple con scripts.

**E:** ¿Algún snippet útil para CLI?
**I:** Un script que lee stdin, llama a la API y devuelve el texto. Así puedo encadenarlo con pipes de shell.

---

## 5) Cierre y reto
**E:** ¿Qué puede probar el oyente hoy?
**I:** Crea un alias `git-commit-ai` que lea `git diff --staged` y te suelte un mensaje sugerido. Segundo reto: pásale tu `server.log` y pídele un resumen con errores y endpoints afectados.

**E:** ¿Se necesita GPU o un modelo local?
**I:** No. Empieza con API: velocidad, coste bajo y cero fricción. Si luego quieres privacidad o coste fijo, miras modelos locales.
