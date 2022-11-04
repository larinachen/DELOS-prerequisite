import socket
import os
import sys
import time

HOST = "my-server-service" # '127.0.0.1'  # The server's hostname or IP address
PORT = 9999       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024).decode("utf-8")

print(f"Message from server: {data!r}")


'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

'''



'''

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

done = False

while not done:
    print("connecting to " + HOST + " at port " + str(PORT))

    client.send("Roger".encode("utf-8"))

    msg_received = client.recv(1024).decode("utf-8")

    if msg_received:
        print(msg_received)

'''



'''
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 30152       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world. IPC success!')
    data = s.recv(1024)

print('Received', repr(data))
'''



'''

counter = 0

SRV = "my-server-service" # os.getenv('SERVER_ADDRESS')
PORT = 30152 # int(os.getenv('SERVER_PORT'))

while 1:
    if counter != 0:
        time.sleep(5)

    counter += 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SRV, PORT)
    print("Connection #{}".format(counter))
    print('Connecting to {} port {}'.format(*server_address))
    try:
        sock.connect(server_address)
    except Exception as e:
        print("Cannot connect to the server,", e)
        continue

    try:
        message = b'This is the message. It will be repeated.'
        print('Sending:  {!r}'.format(message))
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(64)
            amount_received += len(data)
            print('Received: {!r}'.format(data))
    finally:
        print('Closing socket\n')
        sock.close()
'''