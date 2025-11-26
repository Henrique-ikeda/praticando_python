def verificador(cpf):
    if len(cpf) != 11:
        return ("ERRO: o CPF deve ter exatamente 11 dígitos.")
    if not cpf.isdigit():
            return ("Erro: O CPF deve conter apenas números.")
    return ("CPF válido")
