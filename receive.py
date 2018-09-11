#/usr/bin/python

import socket
import sys

def receive(argv):
	UDP_IP_SEND = "10.0.0.1"
	UDP_IP = argv[0]
	UDP_PORT = 5050
	MESSAGE = "Hello, World"

	#print "\n", UDP_IP
	#print "\n", UDP_PORT
	#print "\n", MESSAGE

	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((UDP_IP,UDP_PORT))

	while True:
		data, addr = sock.recvfrom(1024)
		print "received message:", data
		sock.sendto(MESSAGE, (UDP_IP_SEND,UDP_PORT))

if __name__ == "__main__":
	receive(sys.argv[1:])
