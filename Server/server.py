import socket

HOST = socket.gethostbyname('server')  # Standard loopback interface address (localhost)
PORT = 9000                            # Port to listen on (non-privileged ports are > 1023)

filename='/server/send.txt'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(3)
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        while True:
            f = open(filename,'rb')
            #l = f.read(21)
            while (f):
               conn.sendfile(f, 0, 21)
               print('Sent ',repr(f))
               #l = f.read(21)
               f.close()
               break
            break