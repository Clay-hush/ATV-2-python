soma = 0
maior = None
menor = None

for contador in range(1, 6):
    numero = float(input(f"Digite o {contador} numero: "))

    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 5

print(f"Soma: {soma:.2f}")
print(f"Media: {media:.2f}")
print(f"Maior numero: {maior:.2f}")
print(f"Menor numero: {menor:.2f}")