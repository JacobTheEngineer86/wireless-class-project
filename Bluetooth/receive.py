"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

# The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
# 'b8:27:eb:f2:cd:2b'  X'b8:27:eb:f2:cd:2b'  'B8:27:EB:0D:32:D4'  X'b8:27:eb:22:93:39'
hostMACAddress = 'B8:27:EB:0D:32:D4'
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
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
