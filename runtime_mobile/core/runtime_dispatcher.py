class MobileRuntimeDispatcher:
    """
    Dispatcher pre mobilný runtime GAMA.
    Smeruje udalosti na registrované handlery.
    """

    def __init__(self):
        # Mapa event_type → handler funkcia
        self.handlers = {}

    def register_handler(self, event_type: str, handler):
        """
        Registruje handler pre daný typ udalosti.
        Handler musí byť funkcia alebo callable objekt.
        """
        self.handlers[event_type] = handler

    def register_handlers(self):
        """
        Miesto, kde sa budú registrovať všetky handlery.
        Zatiaľ prázdne – doplníš neskôr podľa modulov.
        """
        pass

    def dispatch(self, event):
        """
        Spracuje udalosť podľa jej typu.
        Ak handler existuje → zavolá ho.
        Ak nie → vráti None.
        """
        handler = self.handlers.get(event.type)

        if handler:
            return handler(event)

        # Žiadny handler pre tento event
        return None
