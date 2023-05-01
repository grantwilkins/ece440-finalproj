import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
import lights_client
import random
import time

kivy.require('2.0.0')


def button_click(button_num):
    lights_client.toggle_lights("gfwilki", button_num)


Builder.load_string("""
<MainLayout>:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'

    Label:
        text: 'Button GUI'
        font_size: '24sp'

    Button:
        text: 'Lights 1'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.298, 0.686, 0.314, 1
        on_press: app.on_button_click(1)

    Button:
        text: 'Lights 2'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.298, 0.686, 0.314, 1
        on_press: app.on_button_click(2)

    Button:
        text: 'Lights 3'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.298, 0.686, 0.314, 1
        on_press: app.on_button_click(3)

    # Add the new button with the text "rm -rf /"
    Button:
        text: 'sudo hack kcwang@clemson.edu'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.9, 0.1, 0.1, 1
        on_press: app.dangerous_command_button();
""")



class MainLayout(BoxLayout):
    pass


class ButtonGUIApp(App):
    def build(self):
        return MainLayout()

    def on_button_click(self, button_num):
        button_click(button_num)

    def dangerous_command_button(self):
        while True:
            rand = random.randint(1, 3)
            button_click(rand)


if __name__ == '__main__':
    ButtonGUIApp().run()
