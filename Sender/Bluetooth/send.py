"""
A simple Python script to send messages to a server over Bluetooth
using PyBluez (with Python 2).
"""

# import bluetooth

# serverMACAddress = 'B8:27:EB:0D:32:D4'  # 'b8:85:84:b9:2e:9d'
# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))
# while 1:
#     # text = raw_input()
#     # if text == "quit":
#     #     break
#     text = "Test text - Hello!"
#     s.send(text)
# s.close()


import bluetooth

# 'b8:85:84:b9:2e:9d'  X'b8:27:eb:f2:cd:2b'  'B8:27:EB:0D:32:D4'  X'b8:27:eb:22:93:39'
serverMACAddress = 'b8:27:eb:f2:cd:2b'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

print("Sending Data ...")
while 1:
    # text = raw_input()
    # if text == "quit":
    #     break
    text = "Test text - Hello!"
    s.send(text)
s.close()
