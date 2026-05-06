class MobileRuntimeContext:
    """
    Základný kontext pre mobilný runtime GAMA.
    Uchováva stav, konfiguráciu a runtime premenné.
    """

    def __init__(self):
        # Hlavný stav runtime
        self.state = {
            "initialized": False,
            "active_module": None,
            "last_event": None,
        }

        # Konfigurácia runtime (možno rozšíriť)
        self.config = {
            "version": "1.0.0",
            "platform": "mobile",
            "debug": False,
        }

    def load(self):
        """
        Inicializácia kontextu pri štarte runtime.
        Sem môžeš neskôr doplniť:
        - načítanie uloženého stavu
        - načítanie konfigurácie
        - inicializáciu modulov
        """
        self.state["initialized"] = True

    def set_active_module(self, module_name: str):
        """Nastaví aktuálne aktívny modul."""
        self.state["active_module"] = module_name

    def update_last_event(self, event_type: str):
        """Uloží posledný spracovaný event."""
        self.state["last_event"] = event_type

    def get_state(self):
        """Vráti celý stav runtime."""
        return self.state

    def get_config(self):
        """Vráti konfiguráciu runtime."""
        return self.config

