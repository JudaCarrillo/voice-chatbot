from business_logic import BusinessLogic
from voice_chat import VoiceChat


class VoiceChatBot:
    def __init__(self):
        """Initialize chatbot components."""
        self.voice_chat = VoiceChat()
        self.logic = BusinessLogic(self.voice_chat)

    def run(self):
        """Main function to start the chatbot interaction."""
        self.voice_chat.speak("Bienvenido a Calypso")
        self.voice_chat.speak("¿Qué tipo de servicio desea solicitar?")
        self.voice_chat.speak("Compras, Mantenimiento o Reclamos")

        while True:
            audio = self.voice_chat.listen()
            text = self.voice_chat.recognize_audio(audio)

            if text is None:
                continue

            if not self.logic.process_request(text):
                continue

            self.voice_chat.speak(f"¿Está seguro de que desea pasar con el área de {text}? Responda sí o no.")
            audio = self.voice_chat.listen()
            confirm_text = self.voice_chat.recognize_audio(audio)
            if confirm_text is None:
                self.voice_chat.speak("Seleccione el servicio nuevamente.")
                self.voice_chat.speak("Compras, Mantenimiento o Reclamos")
                continue

            print(f"Respuesta de confirmación: {confirm_text}")

            if self.logic.confirm_choice(confirm_text):
                self.voice_chat.speak("Opción confirmada. Procediendo con su solicitud.")
                break


if __name__ == "__main__":
    print("Iniciando chatbot...")
    chatbot = VoiceChatBot()
    chatbot.run()
