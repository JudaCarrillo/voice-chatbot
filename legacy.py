# import speech_recognition as SR
# import pyttsx3
#
# # Inicialización de reconocimiento y motor de voz
# recognizer = SR.Recognizer()
# engine = pyttsx3.init()
#
# # Configuración del motor de voz
# engine.setProperty("rate", 150)  # Velocidad de la voz
# engine.setProperty("volume", 1)  # Volumen de la voz
#
#
# def speak(text):
#     """Función para sintetizar el texto a voz."""
#     engine.say(text)
#     engine.runAndWait()
# 8
#
# def listen_for_audio():
#     """Función para escuchar el audio del micrófono."""
#     with SR.Microphone() as source:
#         print("Escuchando...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     return audio
#
#
# def recognize_audio(audio):
#     """Función para reconocer el audio y devolver el texto."""
#     try:
#         print("Reconociendo la voz...")
#         text = recognizer.recognize_google(audio, language="es-ES")
#         return text
#     except SR.UnknownValueError:
#         print("No se pudo entender el audio")
#         speak("No se pudo entender lo que dijo, por favor intente de nuevo")
#         return None
#     except SR.RequestError as e:
#         print(f"Error al conectarse con el servicio de reconocimiento de voz: {e}")
#         speak("Hubo un error al conectar con el servicio, por favor intente más tarde")
#         return None
#
#
# def confirm_choice(area):
#     """Función para confirmar la elección del área."""
#     speak(f"¿Está seguro de que desea pasar con {area}? Responda sí o no.")
#     audio = listen_for_audio()
#     text = recognize_audio(audio)
#
#     if text is None:
#         return False
#
#     text = text.lower()
#     if "sí" in text or "si" in text:
#         speak(f"Le paso con {area}")
#         return True
#     elif "no" in text:
#         speak("Por favor, elija una opción nuevamente.")
#         return False
#     else:
#         speak("No entendí la respuesta")
#         return confirm_choice(area)
#
#
# def process_request(text):
#     """Función para procesar la solicitud del usuario según el texto reconocido."""
#     words = text.lower().split()
#
#     if any(word in words for word in ["compras", "compra"]):
#         if confirm_choice("compras"):
#             speak("Le paso con compras")
#         return True
#
#     elif any(word in words for word in ["mantenimiento", "mantenimientos"]):
#         if confirm_choice("mantenimiento"):
#             speak("Le paso con mantenimiento")
#         return True
#
#     elif any(word in words for word in ["reclamos", "reclamo"]):
#         if confirm_choice("reclamos"):
#             speak("Le paso con reclamos")
#         return True
#
#     else:
#         speak("Opción no reconocida, intente nuevamente")
#         return False
#
#
# def main():
#     """Función principal para controlar el flujo del sistema."""
#
#     speak("Bienvenido al Sistema")
#     speak("¿Qué tipo de servicio desea solicitar?")
#     speak("Compras, Mantenimiento o Reclamos")
#
#     # while True:
#     #     audio = listen_for_audio()
#     #
#     #     text = recognize_audio(audio)
#     #
#     #     if text:
#     #         print("Texto reconocido:", text)
#     #
#     #         is_valid = process_request(text)
#     #
#     #         if is_valid:
#     #             break
#     #
#     #         print("Intentando nuevamente...")
#
#
# if __name__ == "__main__":
#     main()