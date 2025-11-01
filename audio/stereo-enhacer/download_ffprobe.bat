@echo off
setlocal

echo Descargando ffmpeg, ffplay y ffprobe...

curl -L -o ffmpeg.exe https://www.gyan.dev/ffmpeg/builds/bin/ffmpeg.exe
curl -L -o ffplay.exe https://www.gyan.dev/ffmpeg/builds/bin/ffplay.exe
curl -L -o ffprobe.exe https://www.gyan.dev/ffmpeg/builds/bin/ffprobe.exe

echo Descarga completa.
pause
