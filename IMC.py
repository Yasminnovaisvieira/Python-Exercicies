# Escreva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O usuário deve informar seu peso em kg e altura em metros. A resposta deve ter no máximo 2 dígitos decimais.

print(f"Olá! O programa irá calcular o índice de Massa Corporal (IMC).\n")

peso = float(input("Insira o peso (KG): "))
altura = float(input("Insira a altura (Metros): "))

imc = peso / (altura * altura)

print(f"\nSeu IMC é: {imc:.2f}")