import paho.mqtt.client as mqtt
from .models import Data
import json

mqtt_broker = "ia.ic.polyu.edu.hk"  # Broker
mqtt_port = 1883  # Default
mqtt_qos = 1  # Quality of Service = 1
mqtt_topic = "IC/123"

alert = False
countOff = 0

def mqtt_on_message(client, userdata, msg):
    global alert
    global countOff
    # Do something
    try:
        d_msg = str(msg.payload.decode("utf-8"))
        m5Data = json.loads(d_msg)
        # if iotData["id"] == ID:
        #     print("Received message on topic %s : %s" % (msg.topic, iotData))
        #
        print("bibibibibibi")
        counter = m5Data["MOVED"]
        if counter == "Yes":
            countOff = 5
            alert = True
        if counter == "No" and countOff >= 0:
            countOff -= 1
        if countOff <= 0:
            alert = False
    except (json.decoder.JSONDecodeError,  KeyError):
        print("Wrong data received in M5.")
    



mqtt_client = mqtt.Client("BANANANANANNA")  # Create a Client Instance
mqtt_client.on_message = mqtt_on_message
mqtt_client.connect(mqtt_broker, mqtt_port)  # Establish a connection to a broker
print("Connect to M5 MQTT broker")
mqtt_client.subscribe(mqtt_topic, mqtt_qos)

mqtt_client.loop_start()
