tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "lossiogay":
        print("acesso concedido!")
        break
    else: 
        print("Senha incorreta. Tente novamente")
        tentativas += 1
else:
    print("Você excedeu o número máximo de tentativas")