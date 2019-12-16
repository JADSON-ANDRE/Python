# -*- coding: utf-8 -*-
import socket
import sqlite3

class Cliente:
	def __init__(self, IP):
		self.IP = IP
		self.total = 0
		self.listaDeBebidas = []
		self.listaDeFrutas = []
		self.cenario = '0'
		self.telaTres = '0'

	def setTotal(self, preco):
		self.total = self.total + preco
	def setListaDeBebidas(self, bebida):
		self.listaDeBebidas.append(bebida)
	def setListaDeFrutas(self, fruta):
		self.listaDeFrutas.append(fruta)
	def setCenario(self, cen):
		self.cenario = cen
	def setTelaTres(self, t):
		self.telaTres = t
	def getIP(self):
		return self.IP
	def getTotal(self):
		return self.total
	def getListaDeBebidas(self):
		return self.listaDeBebidas
	def getListaDeFrutas(self):
		return self.listaDeFrutas
	def getCenario(self):
		return self.cenario
	def getTelaTres(self):
		return self.telaTres	
	

def telaInicial():
	return 'DJ_Drinks\n\n1 - Fruta\n2 - Bebida\n3 - Preços\n4 - SAIR\n'

def telaDeFrutas(cursor):
	cursor.execute("""
		SELECT * from tb_frutas;
		""")
	respostaAux = cursor.fetchall()
	if not respostaAux:
		resposta = "Nenhuma fruta cadastrada"
	else:
		resposta = []
		for item in respostaAux:
			resposta.append(item)
	return resposta

def telaDeBebidas(cursor):
	cursor.execute("SELECT * FROM tb_bebidas;")
	respostaAux = cursor.fetchall()
	if not respostaAux:
		resposta = "Nenhuma bebida cadastrada"
	else:
		resposta = []
		for item in respostaAux:
			resposta.append((item))	
	return resposta

def telaDePrecos(cursor):
	resposta = []
	resposta.append(telaDeFrutas(cursor))
	resposta.append(telaDeBebidas(cursor))
	return resposta

def verificaFruta(data, cursor):
	y = int(data)
	cursor.execute("SELECT id, nome, preco FROM tb_frutas")
	x = []
	for i in cursor:
		if(int(i[0]) == y):
			x.append(i[1])
			x.append(i[2])
	return x

def verificaBebida(data, cursor):
	y = int(data)
	cursor.execute("SELECT id, nome, preco FROM tb_bebidas")
	x = []
	for i in cursor:
		if(int(i[0]) == y):
			x.append(i[1])
			x.append(i[2])
	return x


conn = sqlite3.connect('drinks.db')

conn.text_factory = str #faz eliminar caracteres ("lixos") do database nas strings

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_frutas (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	preco DOUBLE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_bebidas (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	preco DOUBLE NOT NULL
);
""")


cursor.execute("INSERT INTO tb_frutas (nome, preco) VALUES ('abacaxi', 3.00);");
cursor.execute("INSERT INTO tb_frutas (nome, preco) VALUES ('banana', 3.50);");
cursor.execute("INSERT INTO tb_frutas (nome, preco) VALUES ('caja', 4.50);");

'''
cursor.execute("DELETE FROM tb_frutas WHERE nome = 'abacaxi'");
cursor.execute("DELETE FROM tb_frutas WHERE nome = 'banana'");
cursor.execute("DELETE FROM tb_frutas WHERE nome = 'caja'");
'''

cursor.execute("INSERT INTO tb_bebidas (nome, preco) VALUES ('bacardi', 5.00);");
cursor.execute("INSERT INTO tb_bebidas (nome, preco) VALUES ('conhaque', 3.00);");
cursor.execute("INSERT INTO tb_bebidas (nome, preco) VALUES ('espumante', 10.00);");



UDP_IP = "localhost"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

listaClientes = []

while True:
	data, addr = sock.recvfrom(1024)
	resposta = ""
	x = -1
	print (addr)
	for i in listaClientes:
		x = x + 1
		if i.getIP() == addr:
			if i.getCenario() == '0':
				if i.getTelaTres() == '0':
					i.setCenario(data)
				else:
					i.setTelaTres('0')
					resposta = telaInicial()
					break
			if i.getCenario() == '1':
				#mostro a tabela de frutas e atualizo o cenario para 5 (escolhendo fruta)
				i.setCenario('5')
				resposta = "Escolha a opção de fruta\n" + str(telaDeFrutas(cursor)) + "\n"
				#resposta.append(telaDeFrutas(cursor))
			elif i.getCenario() == '2':
				#mostro a tabela de bebidas e atualizo o cenario para 6 (escolhendo bebida)
				i.setCenario('6')
				resposta = "Escolha a opção de bebida desejada\n" + str(telaDeBebidas(cursor)) + "\n" 
			elif i.getCenario() == '3':
				#mostro a tabela de preços e atualizo o cenário para 0 (menu inicial)
				i.setCenario('0')
				resposta = str(telaDePrecos(cursor)) + "\nDigite 0 para retornar ao menu\n"
				i.setTelaTres('1')
			elif i.getCenario() == '4':
				#retorno o valor total e as escolhas do cliente
				#apago este cliente da minha lista
				resposta = "A lista de frutas é: "
				resposta = resposta + str(i.getListaDeFrutas()) + "\nA lista de bebidas é: "
				resposta = resposta + str(i.getListaDeBebidas()) + "\nO total a pagar é: "
				resposta = resposta + str(i.getTotal()) + "\n"
				del(listaClientes[x])
				sent = sock.sendto(str(resposta), addr)
			elif i.getCenario() == '5':
				#armazeno a fruta escolhida na lista de frutas e atualizo o valor deste cliente
				#configuro o cenario deste cliente para (tela inicial) 0
				h = verificaFruta(data, cursor)
				if len(h) > 0:
					i.setListaDeFrutas(h[0])
					i.setTotal(float(h[1]))
					i.setCenario('0')
					resposta = telaInicial()
				else:
					resposta = "Opção inválida\n" + telaInicial()
			elif i.getCenario() == '6':
				#armazeno a bebida escolhida na lista de bebidas e atualizo o valor deste cliente
				#configuro o cenario deste cliente para (tela inicial) 0
				h = verificaBebida(data, cursor)
				if len(h) > 0:
					i.setListaDeBebidas(h[0])
					i.setTotal(float(h[1]))
					i.setCenario('0')
					resposta = telaInicial()
				else:
					resposta = "opção inválida\n" + telaInicial()
			break
	#Se cheguei aqui não encontrei tal cliente, logo esta é a primeira requisição!	
	#adiciono o addr do cliente na listaEndCliente
	#configuro o cenario deste cliente para (tela inicial) 0
	#mostro a tela inicial para este cliente
	x = x + 1
	if x != 0:
		sent = sock.sendto(str(resposta), addr)
	else:
		c = Cliente(addr)
		listaClientes.append(c)
		resposta = telaInicial()
		sent = sock.sendto(str(resposta), addr)
	conn.commit()
conn.close()
