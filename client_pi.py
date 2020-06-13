#!/usr/bin/env python

import os
import socket
import sys
import time
import fileinput

pi_ip = os.environ["PI_IP"]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((pi_ip, 8268))

for line in sys.stdin:
    broke_up_line = line.split(";")
    broke_up_lines = line.splitlines()
    print(len(broke_up_line))
    print(len(broke_up_lines))
    print(broke_up_lines)
    client_socket.sendall(line.encode("UTF-8"))

#send disconnect message
dmsg = "disconnect"
print("Disconnecting")
client_socket.send(dmsg)

client_socket.close()
