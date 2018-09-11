#/usr/bin/python

import socket
import sys
import time

def send(argv):
	UDP_IP = argv[1]
	UDP_PORT = 5050
	UDP_IP_recv = "10.0.0.1"
	#UDP_PORT_recv = 5051
	MESSAGE = "Hello, World"
	
	print "\n", UDP_IP
	print "\n", UDP_PORT
	print "\n", MESSAGE

	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((UDP_IP_recv,UDP_PORT))
	while True:
		time1 = time.time()
		sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
		data, addr = sock.recvfrom(1024)
		time2 = time.time()
		#print "time1\n", time1
		#print "time2\n", time2
		print "time1-time2\n", (time2-time1)*1000
		time.sleep(0.1)
if __name__ == "__main__":
	send(sys.argv)
