import time
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))


def MQTT_publish(broker, file, topic):
    client = mqtt.Client()
    print("Connecting to broker", broker)
    client.connect(broker)
    client.loop_start()
    print("Publishing...")

    myfile = open(file, 'rb')
    Lines = myfile.readline()
    for line in Lines:
        print(line)
        client.publish(f"{topic}", str(line))
        time.sleep(3)


broker = "mqtt.eclipseprojects.io"

MQTT_publish(broker, "data.ods", "topic")
