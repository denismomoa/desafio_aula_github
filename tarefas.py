# Algoritmo: Média Escolar

prova1: float
prova2: float
media: float

prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))

media = (prova1 + prova2) / 2
print(f"Sua média é: {media:,.2f}")