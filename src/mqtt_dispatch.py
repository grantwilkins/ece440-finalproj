import paho.mqtt.client as mqtt

client = None
# Setup callback functions that are called when MQTT events happen like
# connecting to the server or receiving data from a subscribed feed.
def on_connect(client, userdata, flags, rc):
   print("Connected with result code " + str(rc))
   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("/leds/pi")

def on_message(client, userdata, msg):
   print(msg.topic+" "+str( msg.payload))

def setup_mqtt():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('localhost', 1883, 60)
    # Connect to the MQTT server and process messages in a background thread.
    client.loop_start()

# Main loop to listen for button presses.
def toggle_lights(data):
    global client
    if (data == 1):
        client.publish('/leds/esp8266_1', 'TOGGLE')
    elif(data == 2):
        client.publish('/leds/esp8266_2','TOGGLE')
    elif(data == 3):
        client.publish('/leds/esp8266_3','TOGGLE')
    else:
        print("Invalid data")