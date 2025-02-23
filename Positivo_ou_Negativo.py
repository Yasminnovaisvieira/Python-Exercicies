# Verifique se pelo menos um dos valores é negativo.

print(f"Olá! O programa irá verificar se os valores são NEGATIVOS. ")

valor1 = int(input("Declare o 1º número:"))
valor2 = int(input("Declare o 2º número:"))

if valor1 < 0 and valor2 < 0:
    print(f"Ambos os números, {valor1} e {valor2}, são NEGATIVOS.")
elif valor1 < 0:
    print(f"{valor1} é NEGATIVO, porém {valor2} não é.")
elif valor2 < 0:
    print(f"{valor2} é NEGATIVO, porém {valor1} não é.")
else:
    print(f"Os números {valor1} e {valor2} não são negativos.")
