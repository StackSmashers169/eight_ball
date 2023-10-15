import socket
from server import ADDRESS

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)

message = input()

while message.lower() in ["quit", "exit"]:
    print("Exit request sent to server, closing client")
    break

client_socket.close()
