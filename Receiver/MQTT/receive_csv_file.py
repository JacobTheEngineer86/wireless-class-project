import time
import paho.mqtt.client as mqtt


def MQTT_publish(broker, file, topic):
    client = mqtt.Client()
    print("Connecting to broker", broker)
    client.connect(broker)
    client.loop_start()
    print("Publishing...")

    client.loop_start()
    with open(file, 'r') as read_obj:
        data = reader(read_obj)
        for row in data:
            client.publish(f"{topic}", str(row))
            time.sleep(5)
    client.loop_stop()


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))


def MQTT_subscribe(broker, topic):
    client = mqtt.Client()
    print("Connecting to broker", broker)
    client.connect(broker)

    print(f"Subscribing {topic}")
    client.subscribe(f"{topic}")
    client.on_message = on_message
    client.loop_forever()


broker = "mqtt.eclipseprojects.io"

MQTT_subscribe(broker, "topic")
