import socket
import threading


HOST = '127.0.0.1'
PORT = 55555
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
clients = []
print(f"Server is listening on {HOST}:{PORT}")

def handle_client(client_socket, addr):
    print(f"Connected: {addr}")

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            # print(f"Received from {addr}: {data}")
            broadcast(data)
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Disconnected: {addr}")
    client_socket.close()


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error broadcasting message: {e}")
            client.close()
            clients.remove(client)


while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
