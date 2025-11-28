def iu():
    x = True
    num = 0
    print("== Contador de cédulas únicas==")
    try:
        while x:
            num = int(input("Digite o valor do saque:"))
            if num <= 0:
                print("O valor não pode ser negativo nem 0")
            elif num % 2 == 0:
                calculando_notas(num)
            else:
                print("Erro: O valor deve ser múltiplo de 2.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        iu()


def calculando_notas(num):
    cedulas = [100, 50, 20, 10, 5, 2]
    for cedula in cedulas:
        quantidade = num//cedula  # divisão inteira
        if quantidade > 0:
            print(f"{quantidade} cédulas de R${cedula}")
            num = num % cedula
