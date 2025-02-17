class BusinessLogic:
    def __init__(self, voice_chat):
        self.voice_chat = voice_chat

        self.options: dict[str, str] = {
            "compras": "Compras",
            "compra": "Compras",
            "mantenimiento": "Mantenimiento",
            "mantenimientos": "Mantenimiento",
            "reclamos": "Reclamos",
            "reclamo": "Reclamos"
        }

    def confirm_choice(self, text) -> bool:
        """Asks the user to confirm their selected area."""
        if "sí" in text or "si" in text:
            return True
        elif "no" in text:
            self.voice_chat.speak("Por favor, elija un servicio nuevamente.")
            return False
        else:
            self.voice_chat.speak("No entendí la respuesta, Por favor, elija un servicio nuevamente.")
            return False

    def process_request(self, text):
        """Processes the user's request based on recognized text."""
        requested_area = None

        for keyword, area in self.options.items():
            if keyword in text:
                requested_area = area
                break

        if not requested_area:
            self.voice_chat.speak("No se reconoció la opción, por favor intente de nuevo")
            return False

        return requested_area
