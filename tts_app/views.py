# views.py

from django.shortcuts import render
from gtts import gTTS
import cloudinary.uploader

def index(request):
    audio_url = None
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            tts = gTTS(text)
            audio_file = cloudinary.uploader.upload(tts, resource_type="raw")
            audio_url = audio_file.get("secure_url")
    return render(request, 'index.html', {'audio_url': audio_url})
