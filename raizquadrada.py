import math
print("Formato: ax2 + bx + c = 0")
a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))

m = math.sqrt(b ** 2)
x = (-b + m) / 2 * a

print("", x)