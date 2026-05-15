import socket
import os
from datetime import datetime


host = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((host, 0))

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("Sniffer Started...")


while True:

    data = s.recvfrom(65565)

    packet = data[0]

    now = datetime.now()

    msg = f"{now} | Packet Length : {len(packet)}"

    print(msg)

    with open("packets.log", "a") as f:
        f.write(msg + "\n")