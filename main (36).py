import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific IP address and port number
server_socket.bind(('127.0.0.1', 8888))

# listen for incoming connections
server_socket.listen(1)

print('Server started, listening for connections...')

while True:
    # accept incoming connections
    client_socket, address = server_socket.accept()
    
    print(f'Connection from {address} has been established!')
    
    # send a welcome message to the client
    message = 'Welcome to the server!'
    client_socket.send(message.encode())
    
    # close the connection with the client
    client_socket.close()
