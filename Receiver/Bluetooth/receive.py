import bluetooth


# 'b8:27:eb:f2:cd:2b'  X'b8:27:eb:f2:cd:2b'  'B8:27:EB:0D:32:D4'  X'b8:27:eb:22:93:39'
hostMACAddress = 'B8:27:EB:0D:32:D4'
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

print("Waiting for Data ...")
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
