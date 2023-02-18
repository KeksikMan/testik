from kivy.app import App
from client import client

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window

Window.size = (360, 640)

class MyApp (App):

    def callback(self, instance, value):
        print('the switch', instance, 'is', value)
        client.send_request("time_switch_off")
        if value:
            self.label_switch.text = "запланированное"
        else:
            self.label_switch.text = "моментальное"
            self.box_off.remove_widget(self.grid_buttons)

    def on_press_num1(self, instance):
        pass

    def btn_clear(self, instance):
        self.label_output.text = 'Очищено'
        self.clear_btn.disabled = True

    def build(self):
        #layouts
        box = BoxLayout(orientation='vertical', size_hint=[.95, .95])
        grid_switch = GridLayout(cols=2, rows=1, size_hint=[1, .2])
        self.box_off = BoxLayout(orientation='vertical')
        box_off1 = BoxLayout(orientation='horizontal', size_hint=[1, .6])
        box_label = BoxLayout(orientation='horizontal', size_hint=[1, .14])

        anchor_layout = AnchorLayout()

        ###
        input = TextInput()
        btn1 = Button(text='SWITCH OFF', on_press=self.btn_press)
        ###d

        # output label + clear button
        self.label_output = TextInput(text='output', disabled=False, halign='center', multiline=False, keyboard_mode='managed')
        box_label.add_widget(self.label_output)
        self.clear_btn = Button(text='очитстить', font_name='ponterbold.ttf', on_press=self.btn_clear, disabled=False, size_hint=[.4, 1])
        box_label.add_widget(self.clear_btn)
        self.box_off.add_widget(box_label)

        # switch + label
        self.label_switch = Label(text='запланированное', font_name='ponterbold.ttf', size_hint=[1, 1])
        switch = Switch(active=True)
        switch.bind(active=self.callback)
        grid_switch.add_widget(switch)
        grid_switch.add_widget(self.label_switch)
        self.box_off.add_widget(grid_switch)

        # buttons (nums, switch off)
        self.grid_buttons = GridLayout(rows=3, cols=3)
        btn_num1 = Button(text='1')
        btn_num2 = Button(text='2')
        btn_num3 = Button(text='3')
        btn_num4 = Button(text='4')
        btn_num5 = Button(text='5')
        btn_num6 = Button(text='6')
        btn_num7 = Button(text='7')
        btn_num8 = Button(text='8')
        btn_num9 = Button(text='9')
        self.grid_buttons.add_widget(btn_num1)
        self.grid_buttons.add_widget(btn_num2)
        self.grid_buttons.add_widget(btn_num3)
        self.grid_buttons.add_widget(btn_num4)
        self.grid_buttons.add_widget(btn_num5)
        self.grid_buttons.add_widget(btn_num6)
        self.grid_buttons.add_widget(btn_num7)
        self.grid_buttons.add_widget(btn_num8)
        self.grid_buttons.add_widget(btn_num9)
        box_off1.add_widget(self.grid_buttons)


        # switch off button
        self.button_switch_off = Button(text='switch off', size_hint=[1, 1])
        box_off1.add_widget(self.button_switch_off)

        # adding wigets
        self.box_off.add_widget(box_off1)
        box.add_widget(self.box_off)
        box.add_widget(input)
        box.add_widget(btn1)


        anchor_layout.add_widget(box)
        return anchor_layout

    def btn_press(self, instance):
        print("конпка")

if __name__ == '__main__':
    MyApp().run()