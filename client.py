import socket
from server import ADDRESS

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)

# prompts client to send message.
welcome_message = client_socket.recv(1024).decode('utf-8')
print(welcome_message)
message = input(" -> ")


while message.lower() not in ["quit", "exit"]:
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    print()  # print empty line for easier reading

    print(welcome_message)
    message = input(" -> ")

print("Exit request sent to server, closing client")
client_socket.close()
