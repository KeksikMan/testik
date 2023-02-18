from kivy.app import App
import client

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window

Window.size = (360, 640)
Window.clearcolor = (55/255, 55/255, 55/255, 1)

class MyApp (App):

    def callback(self, instance, value):
        if not value:
            self.label_output.text = "Переключите режим"
            self.label_output.disabled = True
            self.clear_btn.disabled = True
            self.grid_buttons.disabled = True
            self.label_switch.text = "моментальное"
            self.button_switch_off.disabled = False
            self.box_off.remove_widget(self.grid_buttons)
        else:
            self.button_switch_off.disabled = True
            self.label_output.text = "Задайте кол-во сек."
            self.label_output.disabled = False
            self.grid_buttons.disabled = False
            self.label_switch.text = "запланированное"
    def on_press_num(self, instance):
        if self.label_output.text == "Задайте кол-во сек." or self.label_output.text == "Очищено":
            self.label_output.text = instance.text
            self.clear_btn.disabled = False
        else:
            self.label_output.text += instance.text
        self.button_switch_off.disabled = False
    def btn_clear(self, instance):
        self.label_output.text = 'Очищено'
        self.clear_btn.disabled = True
        self.button_switch_off.disabled = True
    def shutdown(self, instance):

        if not self.switch.active:
            client.send_request("shutdown -s -t 15")
            self.pb_label.text = 'осталось 15 сек'
            self.pb.max = 15
            self.pb.value = 10
        else:
            client.send_request("shutdown -s -t " + self.label_output.text)
            self.pb_label.text = 'осталось ' + self.label_output.text + ' сек'
            self.pb.max = self.label_output.text
            self.pb.value = 10


    def btn_press(self, instance):
        client.send_request("shutdown /a")
    def switch_automode(self, instance, value):
        if value:
            client.send_request("auto mode on")
        else:
            client.send_request("auto mode off")
    def on_slider(self, instance, pos):
        if instance.value//60 != 0:
            value = str(int(instance.value//60))
            if instance.value % 60 != 0:
                value = value + ':' + str(int(instance.value % 60))
            else:
                value = value + ":" + "00"
        else:
            value = "00"
            if instance.value % 60 != 0:
                value = value + ':' + str(int(instance.value % 60))
            else:
                value = value + ":" + "00"
        self.time_output_label.text = value

    def build(self):
        #layouts
        box = BoxLayout(orientation='vertical', size_hint=[.95, .95])
        grid_switch = GridLayout(cols=2, rows=1, size_hint=[1, .2])
        grid_automode_switch = GridLayout(cols=2, rows=1, size_hint=[1, .2])
        self.box_off = BoxLayout(orientation='vertical')
        box_off1 = BoxLayout(orientation='horizontal', size_hint=[1, .6])
        box_label = BoxLayout(orientation='horizontal', size_hint=[1, .14])
        grid_setup_slider = GridLayout(cols=2, rows=1, size_hint=[1, .2])
        box_setup_time = BoxLayout(orientation='vertical', size_hint=[1, .5])
        anchor_pb = AnchorLayout(size_hint=[1, 1])
        box_pb = BoxLayout(orientation='vertical', size_hint=[1, .3], padding=[0, 20, 0, 0])

        anchor_layout = AnchorLayout()



        # cancel shutdown
        btn1 = Button(text='Остановить выключение', on_press=self.btn_press, font_name='ponterbold.ttf', size_hint=[1, .5])
        self.pb = ProgressBar(max=1000, size_hint=[.8, 1])
        self.pb_label = Label(text='осталось ... сек', font_name='ponterbold.ttf', size_hint=[1, 1])
        anchor_pb.add_widget(self.pb)
        box_pb.add_widget(self.pb_label)
        box_pb.add_widget(anchor_pb)

        # on\off auto mode
        self.automode_switch = Switch()
        self.automode_switch.bind(active=self.switch_automode)
        label_automode_switch = Label(text='авто выключение', font_name='ponterbold.ttf')
        grid_automode_switch.add_widget(self.automode_switch)
        grid_automode_switch.add_widget(label_automode_switch)

        # output label + clear button
        self.label_output = TextInput(text='Задайте кол-во сек.', disabled=False, halign='center', multiline=False, keyboard_mode='managed', font_name='ponterbold.ttf')
        box_label.add_widget(self.label_output)
        self.clear_btn = Button(text='очитстить', font_name='ponterbold.ttf', on_press=self.btn_clear, disabled=True, size_hint=[.4, 1])
        box_label.add_widget(self.clear_btn)
        self.box_off.add_widget(box_label)

        # switch + label
        self.label_switch = Label(text='запланированное', font_name='ponterbold.ttf', size_hint=[1, 1])
        self.switch = Switch(active=True)
        self.switch.bind(active=self.callback)
        grid_switch.add_widget(self.switch)
        grid_switch.add_widget(self.label_switch)
        self.box_off.add_widget(grid_switch)

        # buttons (nums, switch off)
        self.grid_buttons = GridLayout(rows=3, cols=3)
        for i in range(1, 10):
            btn = Button(text=str(i), font_name='ponterbold.ttf')
            btn.bind(on_press=self.on_press_num)
            self.grid_buttons.add_widget(btn)
        box_off1.add_widget(self.grid_buttons)

        # shutdown button and progressbar
        self.button_switch_off = Button(text='Выключить', size_hint=[1, 1], font_name='ponterbold.ttf', disabled=True)
        self.button_switch_off.bind(on_press=self.shutdown)
        box_off1.add_widget(self.button_switch_off)

        # adding wigets
        self.box_off.add_widget(box_off1)
        box.add_widget(self.box_off)
        box.add_widget(grid_automode_switch)
        box.add_widget(box_pb)
        box.add_widget(btn1)

        # slider and set up button
        self.slider = Slider(value_track=True, value_track_color=[50/255, 117/255, 125/255, 1], orientation='horizontal', max=1440, min=0, step=10, cursor_image='clock.png', cursor_size=[45,45], size_hint=[1, .3])
        self.slider.bind(on_touch_move=self.on_slider)
        self.slider.bind(on_touch_up=self.on_slider)
        setup_time_btn = Button(text='Установить', font_name='ponterbold.ttf')
        self.time_output_label = Label(text='00:00', font_name='ponterbold.ttf', size_hint=[.65, 1])
        grid_setup_slider.add_widget(self.time_output_label)
        grid_setup_slider.add_widget(setup_time_btn)
        box_setup_time.add_widget(self.slider)
        box_setup_time.add_widget(grid_setup_slider)
        box.add_widget(box_setup_time)


        anchor_layout.add_widget(box)
        return anchor_layout

if __name__ == '__main__':
    MyApp().run()