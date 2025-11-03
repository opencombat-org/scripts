# Episodio 07 — Agentes de IA para automatizar workflows

**E:** ¿Qué es un agente en la práctica?
**I:** Un bucle que decide paso a paso: piensa, elige una herramienta (API/comando), ejecuta y evalúa. Útil para tareas multi-paso como preparar un release.

**E:** ¿Cómo evitar que haga locuras?
**I:** Defino herramientas con contratos estrictos, límites de tiempo/iteraciones y un simulador/sandbox. Logueo cada acción para auditar.

**E:** ¿Caso de uso concreto?
**I:** “Revisa issues abiertos, agrupa por etiqueta, propone changelog y abre un PR con el draft.”

**E:** ¿Cuándo no usar agentes?
**I:** Si el flujo es determinista y corto, un script es mejor y más barato.
