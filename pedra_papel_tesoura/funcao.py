import random
tipos = ["pedra", "papel", "tesoura"]


def escolha_do_computador():
    escolha = random.choice(tipos)
    return escolha


def definindo_ganhador(opcao):
    if opcao not in tipos:
        return ("Escolha invalida")
    escolha = escolha_do_computador()
    print(f"computador escolheu:{escolha}")
    if opcao == escolha:
        print("Empate")
    elif (
        (opcao == "pedra" and escolha == "tesoura") or
        (opcao == "papel" and escolha == "pedra") or
        (opcao == "tesoura" and escolha == "papel")
    ):
        print("Voce venceu!")
    else:
        print("voce perdeu")
