import socket

# Задаем адрес сервера
SERVER_ADDRESS = ('192.168.1.70', 8686)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))
    data = connection.recv(1024)
    print(str(data))
    if str(data) == "b'TCP:Give me string'":
        connection.send(bytes('11111111', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string2'":
        connection.send(bytes('22222222', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string3'":
        connection.send(bytes('33333333', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string4'":
        connection.send(bytes('44444444', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string5'":
        connection.send(bytes('55555555', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string6'":
        connection.send(bytes('66666666', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string7'":
        connection.send(bytes('77777777', encoding='UTF-8'))
    elif str(data) == "b'TCP:Give me string8'":
        connection.send(bytes('88888888', encoding='UTF-8'))
    connection.close()