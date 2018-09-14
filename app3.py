#/usr/bin/python

import socket
import sys
import time
import pandas as pd

class transfers:
	def __init__(self):
		self.UDP_IP_SEND = "10.0.0.2"	
		self.UDP_PORT = 7050
		self.UDP_IP_RECEIVE = "10.0.0.1"
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((self.UDP_IP_RECEIVE,self.UDP_PORT))
	def receive(self):
		global i
		data, addr = self.sock.recvfrom(80000)
		if(data=="okay, its working"):
			i=0
			print "NO"
		#print "received message:", data
	def send(self,data_send):
		self.sock.sendto(data_send, (self.UDP_IP_SEND,self.UDP_PORT))
		
		
if __name__ == "__main__":
	i=1
	file="app3.xlsx"
	writer = pd.ExcelWriter('app3.xlsx', engine = 'xlsxwriter')

	data_set=[]
	init1 = transfers()
	while (True & i):
		init1.receive()
		time1=time.time()
		data_set.append(time1)
		#print ("\n"),i
	init1.sock.close()
	
	#print data_set
	df=pd.DataFrame(data_set)	
	df.to_excel(writer,sheet_name='Sheet1')
	writer.save()
	#init1.sock.close()
