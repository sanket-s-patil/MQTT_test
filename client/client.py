import paho.mqtt.publish as publish
import time
count=0
MQTT_SERVER = "13.59.175.31"
MQTT_PATH = "test_channel"
while 1:
 count=count+1
 print("Sending count...")
 print(count)
 publish.single(MQTT_PATH, count, hostname=MQTT_SERVER)
 time.sleep(1)
 publish.single(MQTT_PATH, "Counter", hostname=MQTT_SERVER)
 time.sleep(1)
