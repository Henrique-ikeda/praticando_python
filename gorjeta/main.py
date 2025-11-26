import calculo
try:
    conta = float(input("Digite o valor da conta:"))
    gorjeta = float(input("Digite a porcentagem de gorjetas:"))
except Exception as e:
    print(f"voce digitou coisa que não podia erro de:{e}")


print(calculo.calcular_gorjeta(conta, gorjeta))
print(calculo.calcular_total(conta, gorjeta))
