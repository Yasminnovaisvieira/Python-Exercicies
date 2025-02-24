# Verifique se pelo menos uma das condições é verdadeira, se valor1  é maior que 3 ou se valor2 é menor que 4.

print("Olá! O programa irá verificar se há condições VERDADEIRAS ao comparar números.")
print("O 1º número inserido será comparado com 3 e o 2º número será comparado com 4.")

valor1 = int(input("Declare o 1º número: "))
valor2 = int(input("Declare o 2º número: "))

aviso = ("O primeiro número não pode ser comparado, pois é igual a 3.\n") * (valor1 == 3) #O * é usado pra fazer o True ou False.
aviso += ("O segundo número não pode ser comparado, pois é igual a 4.\n") * (valor2 == 4)
aviso += (f"Ambas as condições são VERDADEIRAS: {valor1} > 3 e {valor2} < 4.\n") * (valor1 > 3 and valor2 < 4)
aviso += (f"Uma das condições é VERDADEIRA: {valor1} > 3.\n") * (valor1 > 3 and valor2 >= 4)
aviso += (f"Uma das condições é VERDADEIRA: {valor2} < 4.\n") * (valor2 < 4 and valor1 <= 3)
aviso += ("Nenhuma das condições é verdadeira.\n") * (valor1 <= 3 and valor2 >= 4)

print(aviso)