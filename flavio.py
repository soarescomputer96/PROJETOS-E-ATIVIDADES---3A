# calculadora 


def soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado
def subtração(valor1, valor2):
    resultado = valor1 - valor2
    return resultado
def mutiplicação (valor1, valor2):
    resultado = valor1 * valor2
    return resultado
def divisão (valor1, valor2):
    resultado = valor1 / valor2
    return resultado
print("digite os valores:")
valor1 = float(input("digite o número 1: "))
valor2 = float(input("digite o número 2: "))

print("\n")

print("escolha a operação")
print("1 = soma")
print("2 = subtração")
print("3 = multiplicação")
print("4 = divisão")
operação = int(input("opção: ")) 

if operação == 1:
    resultado = soma(valor1, valor2)
    print("\n")
    print("o resultado é:", resultado)
elif operação == 2:
    resultado = subtração(valor1, valor2)
    print("\n")
    print("o resultado é:", resultado)
elif operação == 3:
    resultado = mutiplicação(valor1, valor2)
    print("\n")
    print("o resultado é:", resultado)
elif operação == 4:
    resultado = divisão(valor1, valor2)
    print("\n")
    print("o resultado é:", resultado)

else: print("\n")
print("opção inválida")