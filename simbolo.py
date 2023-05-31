arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
token = ""
estado = 1


# corrigir erros no automato "<>" essa cadeia nao reconhce

for i in range(len(conteudo)):
    caractere = conteudo[i]
    token = token + caractere

    if estado == 1 and caractere == '-':
        estado = 2
    elif estado == 2 and caractere == '-':
        estado = 3
    elif estado == 1 and caractere == '+':
        estado = 4
    elif estado == 4 and caractere == '+':
        estado = 3
    elif estado == 1 and caractere.isdigit():
        estado = 5
    elif estado == 1 and (caractere == ':' or caractere == '<' or caractere == '>'):
        estado = 6
    elif estado == 6 and caractere == '=':
        estado = 5
    elif estado == 6 and caractere == '>':
        estado = 7
    elif estado == 6 and caractere == '<':
        estado = 5

if estado == 2 or estado == 3 or estado == 4 or estado == 5:
    print("Cadeia reconhecida!")
    print(estado)
else:
    print("Cadeia não reconhecida")
    print(estado)
