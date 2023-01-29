import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))

for i in range(1, 3):
    num = int(input(f'Enter {i} number: '))
    client.send(bytes(str(num), encoding='UTF-8'))

for j in range(1, 4):
    print((str(client.recv(1024)).replace("b'", "").replace("'", "")))

client.close()
