import argparse
import time
import bluetooth
import paho.mqtt.client as mqtt

ap = argparse.ArgumentParser()
ap.add_argument("--file", required=True, help='File to Send')
args = vars(ap.parse_args())


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


if args['file'].endswith('ods'):
    print("ods file detected, using MQTT")

    broker = "mqtt.eclipseprojects.io"

    MQTT_publish(broker, "data.ods", "topic")


elif args['file'].endswith('jpg'):
    print("JPEG image detected, using Bluetooth")

    file_to_send = "success.jpg"
    pic = open(file_to_send)

    # 'b8:85:84:b9:2e:9d'  X'b8:27:eb:f2:cd:2b'  'B8:27:EB:0D:32:D4'  X'b8:27:eb:22:93:39'
    serverMACAddress = 'B8:27:EB:0D:32:D4'
    port = 3
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    while 1:

        # text = "Test text - Hello!"
        # s.send(text)
        s.send(pic)

    s.close()


else:
    print("Unsupported file type, try again with jpg or ods file")
