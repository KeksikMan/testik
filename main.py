from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.core.window import Window

Window.size = (500, 500)

class MyApp (App):

    def build(self):
        box = BoxLayout()

        btn = Button(text='Button', on_press=self.btn_press)
        label = Label(text='My programm')

        box.add_widget(btn)
        box.add_widget(label)

        return box

    def btn_press(self, instance):
        print("конпка")

if __name__ == '__main__':
    MyApp().run()