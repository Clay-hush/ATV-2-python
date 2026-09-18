numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))

print("\nEscolha uma operacao:")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

opcao = int(input("Digite a opcao: "))

match opcao:
    case 1:
        resultado = numero_1 + numero_2
        print(f"Resultado da soma: {resultado:.2f}")

    case 2:
        resultado = numero_1 - numero_2
        print(f"Resultado da subtracao: {resultado:.2f}")

    case 3:
        resultado = numero_1 * numero_2
        print(f"Resultado da multiplicacao: {resultado:.2f}")

    case 4:
        if numero_2 != 0:
            resultado = numero_1 / numero_2
            print(f"Resultado da divisao: {resultado:.2f}")
        else:
            print("Nao e possivel dividir por zero.")

    case _:
        print("Opcao invalida.")