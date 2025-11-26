def calcular_gorjeta(conta, gorjeta):
    if gorjeta > 0:
        return (conta * gorjeta)/100
    elif gorjeta <= 0:
        return ("Cliente não quer pagar gorjeta")

def calcular_total(conta, gorjeta):
    if gorjeta > 0 and conta > 0:
        return((conta * (gorjeta+100))/100)
    elif gorjeta <= 0:
        return conta
    elif conta <= 0:
        return("cliente não tem nada a pagar")
