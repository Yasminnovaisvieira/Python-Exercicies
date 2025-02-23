# Calcule a média de 3 valores.

print(f"Olá! O programa irá calcular a média de 3 números. ")

numero1 = float(input("Declare o 1º número:"))
numero2 = float(input("Declare o 2º número:"))
numero3 = float(input("Declare o 3º número:"))

media = (numero1 + numero2 + numero3) / 3

print(f"A média dos números {numero1}, {numero2} e {numero3} é igual a: {media:.2f}") #Limitar números decimais.