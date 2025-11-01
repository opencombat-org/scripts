#!/usr/bin/env python3
"""
Descarga vídeos de YouTube en el formato deseado usando yt-dlp.

Requisitos:
  - Python 3.8+
  - yt-dlp (pip install yt-dlp)
  - ffmpeg (opcional pero recomendado para conversiones de contenedor)

Uso:
  python youtube_downloader.py URL [-o OUTPUT_DIR] [--audio] [--format FORMAT] [--filename NAME]

Ejemplos:
  # Vídeo MP4 de mejor calidad disponible
  python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

  # Solo audio en M4A
  python youtube_downloader.py URL --audio --format m4a

  # Guardar en un directorio y con nombre específico
  python youtube_downloader.py URL -o ./downloads --filename "mi_video"

Nota legal: respeta los términos de servicio de YouTube y los derechos de autor.
"""
import argparse
import os
import sys
from pathlib import Path

try:
    import yt_dlp as ytdlp
except Exception as e:
    print("Error: yt-dlp no está instalado. Instálalo con: pip install yt-dlp")
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Descargar vídeos de YouTube con yt-dlp")
    parser.add_argument("url", help="URL del vídeo o playlist")
    parser.add_argument("-o", "--output", default="./downloads", help="Directorio de salida (por defecto ./downloads)")
    parser.add_argument("--audio", action="store_true", help="Extraer solo audio")
    parser.add_argument("--format", default=None, help="Formato contenedor deseado (mp4, mkv, mp3, m4a, etc.)")
    parser.add_argument("--filename", default=None, help="Nombre base del archivo sin extensión")
    return parser.parse_args()


def build_opts(args):
    outdir = Path(args.output)
    outdir.mkdir(parents=True, exist_ok=True)

    # Plantilla de nombre de archivo
    if args.filename:
        outtmpl = str(outdir / f"{args.filename}.%(ext)s")
    else:
        outtmpl = str(outdir / "%(title)s [%(id)s].%(ext)s")

    opts = {
        "outtmpl": outtmpl,
        "noplaylist": False,
        "postprocessors": [],
        "concurrent_fragment_downloads": 3,
        "continuedl": True,
        "retries": 5,
        "trim_file_name": 200,
    }

    if args.audio:
        # Descargar mejor audio disponible
        opts["format"] = "bestaudio/best"
        # Extraer audio: requiere ffmpeg
        post = {
            "key": "FFmpegExtractAudio",
            "preferredcodec": args.format or "m4a",
            "preferredquality": "0"
        }
        opts["postprocessors"].append(post)
    else:
        # Mejor video+audio, preferir mp4 si es posible
        # yt-dlp decidirá la mejor combinación; si --format se especifica, lo forzamos como contenedor
        opts["format"] = "bv*+ba/best"
        if args.format:
            # Convertir a contenedor específico (requiere ffmpeg)
            opts["postprocessors"].append({
                "key": "FFmpegVideoConvertor",
                "preferedformat": args.format
            })

    return opts


def main():
    args = parse_args()
    ydl_opts = build_opts(args)

    try:
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(args.url, download=True)
            # Mensaje final amigable
            if "_filename" in info:
                print(f"Descargado: {info['_filename']}")
            else:
                # Si es playlist, podemos imprimir el título
                print("Descarga completada.")
    except ytdlp.utils.DownloadError as e:
        print(f"Error de descarga: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
