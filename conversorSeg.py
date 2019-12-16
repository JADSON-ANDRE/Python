segundos = input("Entre com o valor em segundos: ")
s = int(segundos)

dia = s // 86400
restoSegundos = s % 86400
horas = restoSegundos // 3600
restoSegundos = s % 3600
minutos = restoSegundos // 60
restoFinal = restoSegundos % 60

print("", dia, "dias,", horas, "horas,", minutos, "minutos e", restoFinal, "segundos.")