# Descargador de YouTube (yt-dlp)

Este script (`youtube_downloader.py`) permite descargar vídeos de YouTube (y muchos otros sitios soportados por **yt-dlp**) en la mejor calidad disponible o extraer solo el audio.

> **Aviso legal**: utiliza esta herramienta respetando los términos de servicio de cada sitio y los derechos de autor vigentes.

## Requisitos
- Python 3.8 o superior
- [yt-dlp](https://github.com/yt-dlp/yt-dlp):
  ```bash
  pip install yt-dlp
  ```
- **Opcional**: [FFmpeg](https://ffmpeg.org/) para conversiones de contenedor y extracción de audio.

### Instalación de FFmpeg (ejemplos)
- **macOS** (Homebrew):
  ```bash
  brew install ffmpeg
  ```
- **Ubuntu/Debian**:
  ```bash
  sudo apt-get update && sudo apt-get install -y ffmpeg
  ```
- **Windows**: descarga el binario desde la web oficial o usa un gestor (p. ej., `choco install ffmpeg`).

## Uso
```bash
python youtube_downloader.py URL [-o OUTPUT_DIR] [--audio] [--format FORMAT] [--filename NAME]
```

### Parámetros
- `URL`: enlace del vídeo o playlist.
- `-o, --output`: directorio de salida (por defecto `./downloads`).
- `--audio`: extraer solo audio.
- `--format`: contenedor deseado (por ejemplo `mp4`, `mkv`, `mp3`, `m4a`).
- `--filename`: nombre base del archivo sin extensión.

### Ejemplos
- **Vídeo + audio** (mejor calidad):
  ```bash
  python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID
  ```
- **Solo audio** (M4A):
  ```bash
  python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID --audio --format m4a
  ```
- **Directorio y nombre personalizados**:
  ```bash
  python youtube_downloader.py https://www.youtube.com/watch?v=VIDEO_ID -o ./downloads --filename "mi_video"
  ```

## Notas
- El script intenta reanudar descargas interrumpidas y aplica reintentos automáticos.
- Si especificas `--format` en modo vídeo, se intentará convertir el contenedor (requiere FFmpeg).
- Para playlists largas, considera limitar elementos con opciones avanzadas de yt-dlp (p. ej. `--playlist-items`).

## Solución de problemas
- **`yt-dlp no está instalado`**: asegúrate de ejecutar `pip install yt-dlp` en el mismo entorno de Python.
- **`ffmpeg not found`**: instala FFmpeg y añade su binario al `PATH`.
- **Errores de red**: vuelve a intentar; el script ya activa reintentos básicos.
