import socket
from encryption import decrypt

#THIS ONE IS FOR CHECKING LOCAL PC IP ADDRESS
#UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_IP = "127.0.0.2"
UDP_PORT = 1001

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    decrypt()
    data = bytes.decode(decrypt()) #change binary to string so the 'b' before the message wont show
    print("received message: %s" % data)