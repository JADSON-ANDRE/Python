import socket
from datetime import datetime
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    lista = []
    while True:
        msg = con.recv(1) #recebe a mensagem do cliente (1 byte)
	x1 = datetime.now().microsecond
        if msg != 'a':
		x = sum(lista)/1000
    		#print x
    		con.send(str(x))
		break
        #print cliente, msg
	con.send(msg) #reenviando a mensagem (1 byte)
	x2 = datetime.now().microsecond
	lista.append(x2 - x1)
    print 'Finalizando conexao do cliente', cliente
    #print lista
    #print len(lista)		
    con.close()
