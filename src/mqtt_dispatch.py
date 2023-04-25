import time
import paho.mqtt.client as mqtt

client = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe("/leds/pi")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " " + str(msg.payload))
    if msg.payload == b'ON':
        print("Turning on light")
    elif msg.payload == b'OFF':
        print("Turning off light")
    else:
        print("Invalid message")

def setup_mqtt():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_start()

def toggle_lights(light_id):
    global client
    client.publish("/leds/pi", "TOGGLE" + str(light_id))