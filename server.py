import socket
from random import choice

ANSWERS = [
    'It is certain'
    'As I see it, yes'
    'Reply hazy, try again'
    'not counting on it'
    'It is decidedly so'
    'Most likely'
    'Ask again later'
    'My reply is no'
    'Without a doubt'
    'Outlook good'
    'Better not tell you now'
    'My sources say no'
    'Definitely'
    'Yes'
    'Cannot predict now'
    'Outlook is not good'
    'You can rely on it'
    'Signs say yes'
    'Concentrate and ask again'
    'Very doubtful'
]

ADDRESS = 'localhost', 1234


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(ADDRESS)
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()

        initial_message = "Write a message to the eight ball"
        client_socket.send(initial_message.encode())

        # send and recieve responses from client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
