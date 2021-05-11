def tomar_banho():
    print("Tirar a roupa")
    print("Abrir o chuveiro")
    print("Se lavar")
    print("Fechar o chuveiro")
    print("Secar")
    print("Colocar uma roupa íntima")

tomar_banho()

print("\nAgora vou fazer de novo\n")
tomar_banho()

var1 = int(input("Digite num1: "))
var2 = int(input("Digite num2: "))
var3 = var1 + var2

nome = input("Qual o seu nome: ").capitalize()
if var3 >= 10:
    print("É maior ou igual a 10")
else:
    print("é menor que 10")

sujo = input("Você está sujo? S/N")

if sujo == "S":
    tomar_banho()
else:
    print("To vendo que está cheirosinho mesmo!")

tomar_banho()