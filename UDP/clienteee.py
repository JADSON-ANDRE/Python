# -*- coding: utf-8 -*-
import socket

UDP_IP = "localhost"
UDP_PORT = 5005
MESSAGE = '1'

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
menu, addr = sock.recvfrom(1024)

while MESSAGE != '4':	
	MESSAGE = raw_input(menu)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	menu, addr = sock.recvfrom(1024)
menu, addr = sock.recvfrom(1024)
print(menu)




