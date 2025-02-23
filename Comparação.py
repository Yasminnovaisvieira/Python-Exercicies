# Verifique se pelo menos uma das condições é verdadeira, se valor1  é maior que 3 ou se valor2 é menor que 4.

print("Olá! O programa irá verificar se há condições VERDADEIRAS ao comparar números.")
print("O 1º número inserido será comparado com 3 e o 2º número será comparado com 4.")

valor1 = int(input("Declare o 1º número: "))
valor2 = int(input("Declare o 2º número: "))

aviso = "" #Para avisar que um dos números é igual ao 3 ou 4.

if valor1 == 3:
    aviso += "O primeiro número não pode ser comparado, pois é igual a 3."
if valor2 == 4:
    aviso += "O segundo número não pode ser comparado, pois é igual a 4."

if valor1 > 3 or valor2 < 4:
    if valor1 > 3 and valor2 < 4:
        aviso += f"\nAmbas as condições são VERDADEIRAS, pois {valor1} é maior que 3 e {valor2} é menor que 4."
    elif valor1 > 3:
        aviso += f"\nUma das condições é VERDADEIRA, pois {valor1} é maior que 3."
    elif valor2 < 4:
        aviso += f"\nUma das condições é VERDADEIRA, pois {valor2} é menor que 4."
else:
    aviso += "\nNenhuma das condições é verdadeira."

print(aviso)