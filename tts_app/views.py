# views.py

from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings

def index(request):
    audio_url = None
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            tts = gTTS(text)
            audio_file = 'audio.mp3'
            audio_path = os.path.join(settings.MEDIA_ROOT, audio_file)
            tts.save(audio_path)
            audio_url = settings.MEDIA_URL + audio_file
    return render(request, 'index.html', {'audio_url': audio_url})
