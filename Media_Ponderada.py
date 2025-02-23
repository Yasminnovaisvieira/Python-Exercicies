# Crie um programa que calcule a média ponderada de três notas, sendo que as notas têm pesos diferentes.

print(f"Olá! O programa irá calcular a MÉDIA PONDERADA de 3 notas.\n")

nota1 = float(input("Digite a 1ª nota: "))
peso1 = float(input("Digite o peso da 1ª nota: "))

nota2 = float(input("Digite a 2ª nota: "))
peso2 = float(input("Digite o peso da 2ª nota: "))

nota3 = float(input("Digite a 3ª nota: "))
peso3 = float(input("Digite o peso da 3ª nota: "))

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"A média ponderada é: {media_ponderada:.2f}")