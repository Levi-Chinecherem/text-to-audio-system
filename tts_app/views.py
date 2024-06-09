from django.shortcuts import render
from gtts import gTTS
import os

def index(request):
    audio_url = None
    if request.method == 'POST':
        text = request.POST['text']
        tts = gTTS(text)
        audio_file_path = 'static/output.mp3'
        tts.save(audio_file_path)
        audio_url = 'static/output.mp3'
    return render(request, 'index.html', {'audio_url': audio_url})
