import socket
import random

ANSWERS = [
    'It is certain',
    'As I see it, yes',
    'not counting on it',
    'It is decidedly so',
    'Most likely',
    'I think it will happen',
    'My reply is no',
    'Without a doubt',
    'Outlook good',
    'My sources say no',
    'Definitely',
    'Yes',
    'Cannot predict now',
    'Outlook is not good',
    'You can rely on it',
    'Signs say yes',
    'Very doubtful',
    'This is the correct forecast',
    'Absolutely',
    'Absolutely Not',
    'Hah! Good one buddy',
]

NON_QUESTIONS = [
    'Concentrate and ask again',
    'Could you ask that again?',
    'This is not a question, so I cannot give a response',
    'No question mark found.. DOES NOT COMPUTE',
    'I can ask the questions instead if your going to muck around',
    'A computer cannot turn a non question into a question',
    'Have you tried putting a ? on the end?',
    'If you keep this up I will type exit or quit for you',
    'Reply hazy, try again',
]

ADDRESS = 'localhost', 1234


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(ADDRESS)
    server_socket.listen(5)

    client_socket, client_address = server_socket.accept()

    initial_message = "Write a message to the eight ball"
    client_socket.send(initial_message.encode())

    with client_socket:
        print(f"Connection at {ADDRESS} established")
        while True:
            # send and recieve responses from client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            if '?' in data:
                message = random.choice(ANSWERS)
                print(message)
                client_socket.send(message.encode('utf-8'))
            else:
                message = random.choice(NON_QUESTIONS)
                client_socket.send(message.encode('utf-8'))

