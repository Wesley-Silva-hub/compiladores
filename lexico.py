#automato para identificador prestando
arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

palavras = conteudo.split()

for palavra in palavras:
    estado = 1
    for caractere in palavra:
        if estado == 1 and caractere.isalpha():
            estado = 2
            break
        if estado == 2 and (caractere.isalpha() or caractere.isnumeric()):
            estado = 3
            break
        if estado == 2 and caractere == '_':
            estado = 4
            continue
        if estado == 4 and (caractere.isalpha() or caractere.isnumeric()):
            estado = 5
            continue
        if estado == 5 and (caractere.isalpha() or caractere.isnumeric()):
            estado = 5
            break
        if estado == 2 and caractere == '.':
            estado = 6
            continue
        if estado == 6 and caractere.isalpha():
            estado = 7
            break
        if estado == 7 and caractere.isalpha():
            estado = 7
            break
        else:
            estado = -1  # Estado inválido

    if  estado == 2 or estado == 3 or estado == 5 or estado == 7:
        print("Cadeia reconhecida")
        print(estado)
        print(palavra)
    else:
        print("Cadeia não reconhecida")
        print(estado)
        print(palavra)
