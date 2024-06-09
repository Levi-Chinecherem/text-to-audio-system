# views.py

from django.shortcuts import render
from gtts import gTTS
import cloudinary.uploader
import tempfile

def index(request):
    audio_url = None
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            tts = gTTS(text)
            # Create a temporary file to store the audio
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
                tts.write_to_fp(temp_audio)
                temp_audio.close()
                # Upload the temporary audio file to Cloudinary
                audio_file = cloudinary.uploader.upload(temp_audio.name, resource_type="raw")
                audio_url = audio_file.get("secure_url")
    return render(request, 'index.html', {'audio_url': audio_url})
