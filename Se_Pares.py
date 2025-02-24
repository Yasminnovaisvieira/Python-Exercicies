# Verifique se ambos os valores são pares.

print("Olá! O programa irá verificar se dois valores são PARES ou não.\n")

valor1 = int(input("Declare o 1º número: "))
valor2 = int(input("Declare o 2º número: "))

print("Ambos os números são PARES." * (valor1 % 2 == 0 and valor2 % 2 == 0) or
      f"{valor1} é PAR, porém {valor2} não é." * (valor1 % 2 == 0 and valor2 % 2 != 0) or
      f"{valor2} é PAR, porém {valor1} não é." * (valor2 % 2 == 0 and valor1 % 2 != 0) or
      "Os dois números não são pares.")