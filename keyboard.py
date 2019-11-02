from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file("keyboard.kv")
Builder.load_file("textbox.kv")
Builder.load_file("buttonbox.kv")
Builder.load_file("emptySpace.kv")


class Keyboard(AnchorLayout):
    pass


class KeyboardApp(App):
    def build(self):
        return Keyboard()


if __name__ == "__main__":
    KeyboardApp().run()
