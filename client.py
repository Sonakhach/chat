import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555
name = input("Enter your name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))


def receive_messages(client_socket):
    while True:
        try:
          
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()


while True:
    message = input("Enter your message: ") 
    full_message = f"{name}: {message}"  
    client_socket.send(full_message.encode('utf-8'))
