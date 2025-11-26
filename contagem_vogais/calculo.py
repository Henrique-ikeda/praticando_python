def conta_vogais(texto):
    vogais = "aeiou"
    quantidade = 0
    for letra in texto:
        if letra in vogais:
            quantidade += 1
    return quantidade