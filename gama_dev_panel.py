import json
import tkinter as tk
from tkinter import ttk

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.main import create_runtime


def main():
    core = create_runtime()["runtime_core"]
    startup = core.initialize()

    window = tk.Tk()
    window.title("SIRIUS LOCAL AI GAMA – testovací panel")
    window.geometry("640x420")

    controls = ttk.Frame(window, padding=10)
    controls.pack(fill="x")

    output = tk.Text(window, wrap="word", padx=10, pady=10)
    output.pack(fill="both", expand=True)

    def show(result):
        output.delete("1.0", "end")
        output.insert("1.0", json.dumps(result, ensure_ascii=False, indent=2))

    def show_help():
        event = MobileEvent(MobileEventTypes.SHOW_HELP, source="windows_dev_panel")
        show(core.handle_event(event))

    help_button = ttk.Button(controls, text="Pomoc", command=show_help)
    help_button.pack(side="left", padx=(0, 8))
    if startup["status"] != "initialized":
        help_button.state(["disabled"])

    ttk.Button(
        controls, text="Stav Runtime", command=lambda: show(core.get_info())
    ).pack(side="left")

    show(startup)
    window.mainloop()


if __name__ == "__main__":
    main()