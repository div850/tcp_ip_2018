#/usr/bin/python

import socket
import sys
import time
import select as s
import Queue as q
import numpy as np

class transfers:
	def __init__(self):
		self.UDP_IP_SEND = "10.0.0.1"	
		self.UDP_PORT = 7050
		self.UDP_IP_RECEIVE = "10.0.0.2"
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((self.UDP_IP_RECEIVE,self.UDP_PORT))
	def receive(self):
		data, addr = self.sock.recvfrom(1024)
		print "received message:", data
	def send(self,data_send):
		self.sock.sendto(data_send, (self.UDP_IP_SEND,self.UDP_PORT))
		
if __name__ == "__main__":
	
	file="data1.xlsx"
	#writer = pd.ExcelWriter('data1.xlsx', engine = 'xlsxwriter')
	data_set=[];

	#df = pd.DataFrame([10,20,30,40,50])	
#	df.append(df2, ignore_index=True)

	#df.to_excel(writer,sheet_name='Sheet1')
	
	inputvarL = [1000,1000,1000,1000,60000,60000,60000,60000]
	init1=transfers()
	inputs = [init1.sock]	
	i=0
	delay=0.03
	complete=1	
	n=[np.random.bytes(1000),np.random.bytes(60000)]
	send_data=n[0]
	while (True & complete):
		time5=time.time()
		r,w,e = s.select(inputs,[],[],0)
		time6=time.time()
		for rs in r: # iterate through readable sockets
			if rs is s: # is it the server
				print("HI")
				#print('\r{}:'.format(a),'connected')
				#readable.append(c) # add the client
			else:
					
            # read from a client
				data = rs.recv(1024)
				if not data:
					print('disconnected')
					readable.remove(rs)
					#rs.close()
				else:
					time7=time.time()
					print data
					
					if(data =="0"):
						send_data=n[0]
						delay = 0.005
					elif(data=="1"):
						send_data=n[0]
						delay=0.001
						print delay
					elif (data=="2"):
						send_data=n[1]
						print sys.getsizeof(send_data)
						delay=0.03
						print delay
					elif (data=="3"):
						send_data=n[1]
						delay=0.005
						print delay
					elif (data=="4"):
						send_data=n[1]
						delay=0.001
						print delay
					elif (data=="row1"):
						complete=0
					print "TA",(time6-time5)*1000*1000
					print "TB",(time7-time6)*1000*1000

    # a simple spinner to show activity
		#init1.send(np.random.bytes(1000))
		init1.send(send_data)
		i=i+1
		time.sleep(delay)
		print "\n", delay
	init1.send("okay, its working")

