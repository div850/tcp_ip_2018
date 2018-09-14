#/usr/bin/python

import socket
import sys
import time
class transfers:
	def __init__(self):
		self.UDP_IP_SEND = "10.0.0.1"	
		self.UDP_PORT = 5050
		self.UDP_IP_RECEIVE = "10.0.0.2"
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((self.UDP_IP_RECEIVE,self.UDP_PORT))
	def receive(self):
         global data_r
         data, addr = self.sock.recvfrom(60000)
         data_r = data
         print "received message:", data[:50], "\n"
	def send(self,data_send):
         global data_r
         self.sock.sendto(data_r[:10], (self.UDP_IP_SEND,self.UDP_PORT))
		
		
if __name__ == "__main__":
    init1 = transfers()
    while True:
        init1.receive()
        #time.sleep(0.1)
        init1.send("Message sent from receiver")		
    init1.sock.close()
	
