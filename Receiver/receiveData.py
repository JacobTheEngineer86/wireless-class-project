import time
import bluetooth
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

    print(f"Subscribing to {topic}")
    client.subscribe(f"{topic}")
    client.on_message = on_message
    client.loop()


if __name__ == '__main__':

    broker = "mqtt.eclipseprojects.io"
    MQTT_subscribe(broker, "topic")

    # 'b8:27:eb:f2:cd:2b'  X'b8:27:eb:f2:cd:2b'  'B8:27:EB:0D:32:D4'  X'b8:27:eb:22:93:39'
    hostMACAddress = 'B8:27:EB:0D:32:D4'
    port = 3
    backlog = 1
    size = 1024
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)

    print("Waiting for Bluetooth Data ...")
    try:
        client, clientInfo = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data)  # Echo back to client
    except:
        print("Closing socket")
        client.close()
        s.close()
