from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (360, 640)


class MyGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
