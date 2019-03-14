import socket
import sys
import pickle

class Atribute:
    Health = 1000
    mana = 100
    itemid = 20
    hero_name = "slark"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 55555)
print ('connecting to %s port %s' % server_address, file = sys.stderr)
sock.connect(server_address)

try:
    
    # Send data
    variable = Atribute()
    data = pickle.dumps(Atribute)
    print ('sending "%s"' % Atribute)
    sock.sendall(data)
    input("press any key")

finally:
    print ('closing socket', file = sys.stderr)
    sock.close()
