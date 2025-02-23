# Crie um programa que calcule o montante final após um período de tempo com juros compostos. O usuário deve informar o capital, taxa de juros e tempo em anos.

print(f"Olá! O programa irá calcular o Montante Final.\n")

capital = float(input("Digite o capital: "))
taxa = float(input("Digite a taxa de juros (% ao ano): ")) / 100
tempo = int(input("Digite o tempo (anos): "))

montante = capital * (1 + taxa) ** tempo

print(f"O montante final após {tempo} anos será de: R$ {montante:.2f}")