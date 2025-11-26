import random

num_escolhido = random.randint(1, 100)  # Corrigido para 1-100


def ui():
    x = True
    while x:
        valor = input("Tente adivinhar o número (1-100): ")

        if not valor.isdigit():
            print("Entrada inválida: Escreva apenas números.")
            continue

        valor = int(valor)

        if not 1 <= valor <= 100:
            print(
                "Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.")
            continue

        # Chamar o verificador
        opcao = verificador(valor)
        if opcao:
            print("Você acertou!")
            x = False
        else:
            if valor > num_escolhido:
                print("Muito alto! Tente novamente.")
            elif valor < num_escolhido:
                print("Muito baixo! Tente novamente.")


def verificador(valor):
    return num_escolhido == valor
