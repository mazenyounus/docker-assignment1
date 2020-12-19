import socket
import shutil
import time

HOST = socket.gethostbyname('server')  # The server's hostname or IP address
PORT = 9000                            # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #data = s.recv(21)
    with open('received_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(21)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)
            break

print('Received', repr(f))
print('Received', type(f))
 
shutil.move("/client/received_file", "/clientdata/received_file")

t_end = time.time() + 60 * 7
while time.time() < t_end:
    VAR1 = 12