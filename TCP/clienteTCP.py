import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
#print 'Para sair use CTRL+X\n'
#msg = raw_input()
#while msg <> '\x18':
i = 0
msg = 'a'
while i < 1000:
    tcp.send (msg) #mandando a mensagem para o servidor (1 byte)
    msg = tcp.recv(1) #recebendo a mensagem de volta
    print msg
    i = i + 1
    #msg = raw_input()
tcp.send('b')
msg = tcp.recv(1024)
print msg
tcp.close()
