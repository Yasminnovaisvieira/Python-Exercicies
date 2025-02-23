# Calcule o resultado e o resto da divisão entre o dividendo e o divisor. Exiba todas as informações.

print(f"Olá! O programa irá calcular o resultado e o resto da divisão entre o dividendo e o divisor.\n")

dividendo = int(input("Insira o número que será o dividendo:"))
divisor = int(input("Insira o número que será o divisor:"))

resultado = dividendo // divisor
resto = dividendo % divisor

print(f"O RESULTADO da operação é: {resultado}\n O RESTO da operação é: {resto}")