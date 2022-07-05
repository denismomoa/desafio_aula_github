# Algoritmo: Média Escolar

prova1: float
prova2: float
media: float
trabalho: float

prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))
trabalho = float(input("Informe a nota do trabalho: "))

media = (prova1 + prova2 + trabalho) / 3
print(f"Sua média é: {media:,.2f}")