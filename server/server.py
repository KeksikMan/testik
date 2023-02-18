import asyncio
import socket
import script

sock = socket.socket()
sock.bind(("192.168.0.108", 80))
sock.listen()

input_hour = int(input("Когда спать? - "))

#loop = asyncio.get_event_loop()
#asyncio.ensure_future(script.check_time(input_hour))
#loop.run_forever()

while True:
    client,addr = sock.accept()
    print(addr)
    while True:
        try:
            request = client.recv(1024)
            if not request: break
            print(request.decode())

            response = 'ok'
            client.send(response.encode())
        except ConnectionResetError:
            break
    client.close()