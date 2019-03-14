import socket
import pickle
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('localhost',55555)
print(sys.stderr,"%s port %s" % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    print ('menunggu koneksi', file = sys.stderr)
    connection, client_address = sock.accept()

    try:
        print ('koneksi dari', client_address, file = sys.stderr)
        data = connection.recv(600)
        receive = pickle.loads(data)
        print (receive)
        input("press any key")
          
    finally:
        connection.close()