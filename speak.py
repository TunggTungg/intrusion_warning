from gtts import gTTS
import playsound, os, threading

class Speak:
    def __init__(self):
        pass
    def speak(self, text):  # Bella speak to customers
        tts = gTTS(text=text, slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")

    def speak_thread(self, text):
        global speak
        speak = threading.Thread(target=self.speak, args=(text,))
        speak.start()