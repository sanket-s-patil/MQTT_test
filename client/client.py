import paho.mqtt.publish as publish
import time

MQTT_SERVER = "13.59.175.31"
MQTT_PATH = "test_channel"

print("Sending 0...")
publish.single(MQTT_PATH, "0", hostname=MQTT_SERVER)
time.sleep(1)
print("Sending 1...")
publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER)
