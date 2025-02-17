import speech_recognition as SR
from gtts import gTTS
from playsound import playsound


class VoiceChat:
    def __init__(self):
        """Initialize speech recognition and text-to-speech engine."""
        self.recognizer = SR.Recognizer()

    # @staticmethod
    def speak(self, text):
        """Converts text to speech."""
        tts = gTTS(text=text, lang="es")
        tts.save("output.mp3")
        playsound("output.mp3")

    def listen(self) -> str:
        """Captures audio from the microphone."""
        with SR.Microphone() as source:
            print("Escuchando...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    def recognize_audio(self, audio) -> str | None:
        """Converts speech to text."""
        try:
            print("Reconociendo la voz...")
            text = self.recognizer.recognize_google(audio, language="es-ES")
            return text.lower()
        except SR.UnknownValueError:
            print("No se pudo entender el audio")
            self.speak("No se pudo entender lo que dijo, por favor intente de nuevo")
            return None
        except SR.RequestError as e:
            print(f"Error al conectarse con el servicio de reconocimiento de voz: {e}")
            self.speak("Hubo un error al conectar con el servicio, por favor intente más tarde")
            return None
