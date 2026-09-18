senha_correta = "1234"
tentativas = 0
acesso_liberado = False

while tentativas < 3:
    senha = input("Digite sua senha: ")

    tentativas += 1

    if senha == senha_correta:
        acesso_liberado = True
        print("Acesso autorizado!")
        break
    else:
        print(f"Senha incorreta. Tentativa {tentativas} de 3.")

if not acesso_liberado:
    print("Acesso bloqueado. Numero maximo de tentativas atingido.")