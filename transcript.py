#!/usr/bin/python

"""Use speech to text to record live transription and person identification."""

import whisper

#model = whisper.load_model("tiny")
model = whisper.load_model("base")
#model = whisper.load_model("medium")

# transcribe
result = model.transcribe("C:/Users/Utilisateur/Desktop/transcript/filename.mp3")

print(result["text"])

