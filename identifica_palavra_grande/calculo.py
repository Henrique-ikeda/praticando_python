def verificador_de_palavras(texto):
    palavras_grandes = []
    for palavra in texto.split():
        if len(palavra) >= 10:
            palavras_grandes.append(palavra)
    return imprimi_lista(palavras_grandes)


def imprimi_lista(palavras_grandes):
    if palavras_grandes:
        print("Palavras longas encontradas:")
        for palavra in palavras_grandes:
            print(f'{palavra},')
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")
