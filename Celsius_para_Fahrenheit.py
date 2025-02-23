# Escreva um programa que converta uma temperatura digitada de graus Celsius para Fahrenheit.

print(f"Olá! O programa irá converter uma temperatura de graus CELSIUS para FAHRENHEIT.\n")

grau_celsius = float(input("Insira a temperatura em graus Celsius:"))

grau_fahrenheit = (grau_celsius * 9 / 5) + 32

print(f"{grau_celsius} Celsius é igual a {grau_fahrenheit} Fahrenheit.")