# Escreva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O usuário deve informar seu peso em kg e altura em metros. A resposta deve ter no máximo 2 dígitos decimais.

print(f"Olá! O programa irá calcular o índice de Massa Corporal (IMC).\n")

peso = float(input("Insira o peso (KG): "))
altura = float(input("Insira a altura (Metros): "))

imc = peso / (altura * altura)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 16:
	print("Magreza Grave.")
elif imc < 17:
	print("Magreza Moderada.")
elif imc < 18.5:
	print("Magreza Leve")
elif imc < 25:
	print("Saudável.")
elif imc < 30:
	print("Sobrepeso.")
elif imc < 35:
	print("Obesidade Grau I.")
elif imc < 40:
	print("Obesidade Grau II.")
else:
	print("Obesidade Grau III.")