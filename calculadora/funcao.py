def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1-num2


def multiplicar(num1, num2):
    return num1*num2


def dividir(num1, num2):
    return num1/num2


def mostrar_opcao():
    try:
        num1 = float(input("Digite o primeiro número:"))
        opcao = input("Escolha a operação (+, -, *, /):")
        num2 = float(input("Digite o segundo número:"))
        if opcao == "+":
            print(somar(num1, num2))
        elif opcao == "-":
            print(subtrair(num1, num2))
        elif opcao == "*":
            print(multiplicar(num1, num2))
        elif opcao == "/":
            print(dividir(num1, num2))
        else:
            print("Opção inválida")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
