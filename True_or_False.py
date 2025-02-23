# True ou False: valor1 + 15 é igual a valor2 * 3

print(f"Olá! O programa irá verificar se Valor1 + 15 tem o mesmo resultado que Valor2 X 3.\n")

valor1 = int(input("Declare o 1º valor: "))
valor2 = int(input("Declare o 2º valor: "))

resultado = (valor1 + 15) == (valor2 * 3)

print(f"{valor1} + 15 tem o mesmo resultado que  {valor2} X 3?\nResposta: {resultado}.")