import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
import lights_client
import random
import time
import signal

kivy.require('2.0.0')

interrupted = False

def button_click(button_num):
    lights_client.toggle_lights("gfwilki", button_num)

import pyaudio
import numpy as np




Builder.load_string("""
<MainLayout>:
    orientation: 'vertical'
    padding: '20dp'
    spacing: '10dp'

    Label:
        text: 'IoT Smart Home Lighting System' 
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

    Button:
        text: 'Clap Mode'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.298, 0.686, 0.314, 1
        on_press: app.listen_for_claps(app.callback_function)

    Button:
        text: 'Stress Test'
        font_size: '32sp'
        background_normal: ''
        background_color: 0.9, 0.1, 0.1, 1
        on_press: app.dangerous_command_button();
""")
                    
def signal_handler(signal, frame):
    global interrupted
    interrupted = True


class MainLayout(BoxLayout):
    pass


class ButtonGUIApp(App):
    def build(self):
        return MainLayout()

    def on_button_click(self, button_num):
        button_click(button_num)

    def dangerous_command_button(self):
        global interrupted
        interrupted = False
        while not interrupted:
            rand = random.randint(1, 3)
            button_click(rand)
    
    def callback_function(self):
        button_click(1)
        button_click(2)
        button_click(3)

    def detect_clap(self,data,threshold=0.6, rate=44100):
        audio_data = np.frombuffer(data, dtype=np.int16)
        normalized_data = audio_data / (2.0 ** 15)
        volume = np.linalg.norm(normalized_data)
        return volume > threshold

    def listen_for_claps(self,callback):
        global interrupted
        chunk_size = 1024
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=audio_format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk_size)

        print("Listening for claps...")
        interrupted = False
        while True:
            data = stream.read(chunk_size, exception_on_overflow=False)
            if ButtonGUIApp.detect_clap(self,data=data):
                callback()
            if interrupted:
                break
        
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    ButtonGUIApp().run()
