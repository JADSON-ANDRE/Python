tempoAtual = int(input("Quantos minutos jogados? "))
tempoTotal = 90

if tempoAtual < tempoTotal:
	restante = tempoTotal - tempoAtual
	print("Jogo em andamento, restam", restante, "minutos.")
else:
	print("Jogo Encerrado!")