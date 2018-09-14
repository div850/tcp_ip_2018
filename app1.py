#/usr/bin/python

import socket
import sys
import time
import numpy as np
import pandas as pd
import threading as th
class transfers:
    def __init__(self):
        self.UDP_IP_SEND = "10.0.0.2"	
        self.UDP_PORT = 5050
        self.UDP_IP_RECEIVE = "10.0.0.1"
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP_RECEIVE,self.UDP_PORT))
    def receive(self):
        data, addr = self.sock.recvfrom(60000)
        print "received message:", data
        return data
    def send(self,data_send):
        self.sock.sendto(data_send, (self.UDP_IP_SEND,self.UDP_PORT))


def send_msg_thread(sock_obj,delay,no_of_pack,bytes_send):
    i=0
    global data_send_time
    #    no_of_pack=1*1000/0.001
    pre_string=str(0).zfill(bytes_send-sys.getsizeof(str(no_of_pack))+37)
    while(i<no_of_pack):
        time.sleep(delay)
        sock_obj.send(str(i).zfill(sys.getsizeof(str(no_of_pack))-37)+pre_string)
        data_send_time.append([str(i).zfill(sys.getsizeof(str(no_of_pack))-37),time.time()])
        #sock_obj.send("HI")
        print "Message Sent"
        i=i+1
def receive_msg_thread(sock_obj,no_of_pack):
    global data_recv_time
    exit_thread=1
    bytes_with=sys.getsizeof(str(no_of_pack))-37
    while exit_thread==1:
        try:
            sock_obj.sock.settimeout(10)
            data=sock_obj.receive()
            data=data[:bytes_with]
            print data
            data_recv_time.append([data,time.time()])
        except:
            exit_thread=0
            print "Receiver Time-out"
#class transfers1:
#	def __init__(self):
#		self.UDP_IP_SEND = "10.0.0.2"	
#		self.UDP_PORT = 7050
#		self.UDP_IP_RECEIVE = "10.0.0.1"
#		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#		#self.sock.bind((self.UDP_IP_RECEIVE,self.UDP_PORT))
#	def receive(self):
#		data, addr = self.sock.recvfrom(60000)
#		#print "received message:", data
#	def send(self,data_send):
#		self.sock.sendto(data_send, (self.UDP_IP_SEND,self.UDP_PORT))

		
if __name__ == "__main__":
    ex=1	
    
    file="data_set1000_100.xlsx"
    file="data_set1000_5.xlsx"
    file="data_set1000_1.xlsx"
    file="data_set1000_0_5.xlsx"
    data_send_time=[]
    data_recv_time=[]
    
    data_set_end=[]
    
    time3=1
    inputvarL = [1000,1000,1000,1000,60000,60000,60000]
    inputvarI = [0.1,0.005,0.001,0.0005,0.1,0.005,0.001,0.0005]
    inputvar2delay = [1000,2000,3000,1000,2000,3000,1000,1000]
    inputvarI = [0.000001]
    init1=transfers()
    	
    for j in range (0,1):
        n=1000
        print "\n", inputvarL[j]
        print "\n", inputvarI[j]

        p1=th.Thread(target=send_msg_thread, args=(init1,inputvarI[j],n,inputvarL[j]))
        p2=th.Thread(target=receive_msg_thread,args=(init1,n,))

        p1.start()
        p2.start()
    
        p1.join()
        p2.join()

        df=pd.DataFrame(data_recv_time,columns=['packet_id','time'])	
        df1=pd.DataFrame(data_send_time,columns=['packet_id','time'])	
        i=0
        while (i<n):
            
            a=df1[df1['packet_id']==str(i).zfill(sys.getsizeof(str(n))-37)]
            if a.empty:
                data_set_end.append([i,"NA"])
            else:
                b=df[df['packet_id']==str(i).zfill(sys.getsizeof(str(n))-37)]
                if b.empty:
                    #data_set_end.append([i,"NAB"])
                    print("empty")
                else:
                    time_diff=df.iloc[b.index[0],1] - df1.iloc[a.index[0],1]
                    data_set_end.append([i,time_diff])
            i=i+1
#        df.to_excel(writer,sheet_name='Sheet1')
#        writer.save()

        file='data_set_s'+'_'+str(inputvarL[j])+'_'+str(inputvarI[j]) + "_" + str(j) +'.xlsx'
        writer = pd.ExcelWriter(file, engine = 'xlsxwriter')
        df1.to_excel(writer,sheet_name='Sheet1')
        writer.save()

        file='data_set_r'+'_'+str(inputvarL[j])+'_'+str(inputvarI[j]) + "_" + str(j) +'.xlsx'
        writer = pd.ExcelWriter(file, engine = 'xlsxwriter')
        df.to_excel(writer,sheet_name='Sheet1')
        writer.save()

        df2=pd.DataFrame(data_set_end,columns=['packet_id','time'])	
        file='data_set_end'+'_'+str(inputvarL[j])+'_'+str(inputvarI[j]) + "_" + str(j) +'.xlsx'
        writer = pd.ExcelWriter(file, engine = 'xlsxwriter')
        df2.to_excel(writer,sheet_name='Sheet1')
        writer.save()
        
        data1=[]
        print ("Completed")
        #init2.send(str(j))
        time.sleep(5)
	init1.sock.close()


#	file="data_set1000_100.xlsx"
#	file="data_set1000_5.xlsx"
#	file="data_set1000_1.xlsx"
#	file="data_set1000_0_5.xlsx"
#	data_set=[];
#	data_set_1000_5=[];
#	data_set_1000_1=[];
#	data_set_1000_0_5=[];

#	#df = pd.DataFrame([10,20,30,40,50])	
##	df.append(df2, ignore_index=True)

#	#df.to_excel(writer,sheet_name='Sheet1')
#	
#	time3=1
#	inputvarL = [1000,1000,1000,1000,1000,1000]
#	inputvarI = [0.1,0.005,0.001,0.1,0.005,0.001]
#	inputvar2delay = [1000,2000,3000,1000,2000,3000,1000,1000]
#	init1=transfers()
#	init2=transfers1()
#	i=0
#	m=0

#	for j in range (0,6):
#		data=np.random.bytes(inputvarL[j])
#		n=time3/inputvarI[j]	
#		print "\n", inputvarL[j]
#		print "\n", inputvarI[j]
#		i=0		
#		while i<n:
#			time1=time.time()
#			init1.send(data)
#			init1.receive()
#			time2=time.time()
#			time.sleep(inputvarI[j])
#			time_diff = (time2-time1)*1000*1000
#			data_set.append(time_diff)
#			i=i+1
#			if(i%10==0):
#				print str(inputvarL[j]) + "_" + str(inputvarI[j]) +"_" + str(i) + "_" + str(j) 
##		file='data_set'+str(inputvarL[j])+str(inputvarI[j])
#		file='data_set'+'_'+str(inputvarL[j])+'_'+str(inputvarI[j]) + "_" + str(j) +'.xlsx'
#		writer = pd.ExcelWriter(file, engine = 'xlsxwriter')
#		df=pd.DataFrame(data_set)	
#		df.to_excel(writer,sheet_name='Sheet1')
#		writer.save()
#		data_set=[]
#		print ("Completed")
#		init2.send(str(j))
#		time.sleep(5)
#	init2.send("row1")
#	init1.sock.close()
#	init2.sock.close()
