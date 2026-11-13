from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from runtime_mobile.main import create_runtime


class GamaApp(App):
    def build(self):
        self.title = "SIRIUS GAMA"
        runtime = create_runtime()
        self.core = runtime["runtime_core"]
        self.router = runtime["nl_router"]
        ready = self.core.initialize()["status"] == "initialized"

        layout = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(12))
        self.question = TextInput(
            hint_text="Čo vytvára fotosyntéza?",
            multiline=False,
            size_hint_y=None,
            height=dp(52),
            disabled=not ready,
        )
        button = Button(text="Opýtať sa", size_hint_y=None, height=dp(48), disabled=not ready)
        self.answer = Label(
            text="Napíš otázku." if ready else "GAMA sa nepodarilo spustiť.",
            halign="left",
            valign="top",
        )
        self.answer.bind(size=lambda label, size: setattr(label, "text_size", size))
        self.question.bind(on_text_validate=self.ask)
        button.bind(on_release=self.ask)
        actions = BoxLayout(size_hint_y=None, height=dp(48), spacing=dp(8))
        clear_button = Button(text="Vymazať")
        example_button = Button(text="Ukážková otázka", disabled=not ready)
        clear_button.bind(on_release=self.clear)
        example_button.bind(on_release=self.ask_example)
        actions.add_widget(clear_button)
        actions.add_widget(example_button)

        for widget in (self.question, button, actions, self.answer):
            layout.add_widget(widget)
        return layout

    def clear(self, *_):
        self.question.text = ""
        if not self.question.disabled:
            self.answer.text = "Napíš otázku."

    def ask_example(self, *_):
        self.question.text = "Čo vytvára fotosyntéza?"
        self.ask()

    def ask(self, *_):
        question = self.question.text.strip()
        if not question:
            return

        result = self.core.handle_event(self.router.route(question))
        matches = result.get("results", [])
        if matches:
            self.answer.text = "\n\n".join(
                f'{match["answer"]}\nZdroj: {match["source"]}' for match in matches
            )
        else:
            self.answer.text = result.get("message") or "Skús otázku zo školského balíka."


if __name__ == "__main__":
    GamaApp().run()
