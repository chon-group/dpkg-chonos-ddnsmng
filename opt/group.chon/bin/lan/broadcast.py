import socket
import sys

try:
    BOTNAME = sys.argv[1]+" "+sys.argv[2]
    MESSAGE = str.encode(BOTNAME)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(MESSAGE, ("255.255.255.255", 3269))
except:
    sys.exit(1)