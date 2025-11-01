import librosa
import numpy as np
import sys
import tempfile
import soundfile as sf
from pydub import AudioSegment

def pitch_shift_stereo(input_file, output_file_mp3, semitones_left=-0.2, semitones_right=0.2):
    # Convertir MP3 a WAV temporalmente con pydub
    audio = AudioSegment.from_file(input_file)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        audio.export(tmp.name, format="wav")
        tmp_path = tmp.name

    # Cargar audio estéreo
    y, sr = librosa.load(tmp_path, sr=None, mono=False)

    if y.ndim != 2 or y.shape[0] != 2:
        raise ValueError("El archivo debe ser estéreo (2 canales).")

    # Separar canales
    left = y[0]
    right = y[1]

    # Aplicar pitch shift
    left_shifted = librosa.effects.pitch_shift(left, sr=sr, n_steps=semitones_left)
    right_shifted = librosa.effects.pitch_shift(right, sr=sr, n_steps=semitones_right)

    # Combinar canales
    y_shifted = np.vstack([left_shifted, right_shifted]).T

    # Guardar WAV temporal
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        sf.write(temp_wav.name, y_shifted, sr)
        # Convertir a MP3
        processed = AudioSegment.from_wav(temp_wav.name)
        processed.export(output_file_mp3, format="mp3")

    print(f"✅ Archivo generado: {output_file_mp3}")

# Uso
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python pitch_stereo_mp3.py audio_in.mp3 audio_out.mp3")
        sys.exit(1)

    input_mp3 = sys.argv[1]
    output_mp3 = sys.argv[2]

    pitch_shift_stereo(input_mp3, output_mp3)
