import socket
import time
import os

HOST = '0.0.0.0' # '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9999     # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        # print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            conn.sendall(b"Roger")


            print(f"Message from client: {data!r}")

'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

print('Waiting for a connection')

done = False

while not done:

    msg_received = client.recv(1024).decode("utf-8")
    
    if msg_received:
        print(msg_received)

    client.send("Hello world!")
'''


'''
PORT = 30152 # int(os.environ['LISTEN_PORT']) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', PORT)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen()

while True:
    print('\nWaiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(64)
            print('Received {!r}'.format(data))
            if data:
                print('Sending data back to the client')
                connection.sendall(data)
            else:
                print('No data from', client_address)
                break
    finally:
        connection.close()
        '''