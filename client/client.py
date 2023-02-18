import socket

sock = socket.socket()
sock.connect(('192.168.0.108', 80))

def send_request(request):
    sock.send(request.encode())

    #response = sock.recv(1024).decode()
    #print(response)