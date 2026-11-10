import json
import tkinter as tk
from tkinter import ttk

from runtime_mobile.core.event import MobileEvent
from runtime_mobile.core.event_types import MobileEventTypes
from runtime_mobile.main import create_runtime
from runtime_mobile.envoy_client import lookup_beta_entity


def main():
    runtime = create_runtime()
    core = runtime["runtime_core"]
    router = runtime["nl_router"]
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

    input_row = ttk.Frame(window, padding=10)
    input_row.pack(fill="x", before=output)
    entry = ttk.Entry(input_row)
    entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

    def submit(event=None):
        text = entry.get().strip()
        if text and startup["status"] == "initialized":
            show(core.handle_event(router.route(text)))
            entry.delete(0, tk.END)
            entry.focus_set()
        return "break"

    send_button = ttk.Button(input_row, text="Odoslať", command=submit)
    send_button.pack(side="left")

    def read_beta():
        show(lookup_beta_entity(entry.get()))

    ttk.Button(input_row, text="Čítať z BETA", command=read_beta).pack(side="left", padx=(8, 0))
    for control in (entry, send_button):
        control.bind("<Return>", submit)
        control.bind("<KP_Enter>", submit)
    entry.focus_set()

    show(startup)
    window.mainloop()


if __name__ == "__main__":
    main()