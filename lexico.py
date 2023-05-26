#IMPLEMENTACAO DO LEXICO

arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
token = ""

for i in range(len(conteudo)):
    caractere = conteudo[i]
    estado = 1
    token = token + caractere
    #aqui comeca o automato de identificador
    if estado == 1 and caractere.isalpha():
        estado = 2

    elif estado == 2 and caractere == '_':
        estado = 4
    
    elif estado == 2 and caractere == '.':
        estado = 6

    elif estado == 2 and caractere.isalpha():
        estado = 2
        
    elif estado == 2 and (caractere.isalpha() or caractere.isnumeric()):
        estado = 3

    elif estado == 3 and (caractere.isalpha() or caractere.isnumeric()):
        estado = 3

    elif estado == 4 and (caractere.isalpha() or caractere.isnumeric()):
        estado = 5

    elif estado == 5 and (caractere.isalpha() or caractere.isnumeric()):
        estado = 5
        
    elif estado == 6 and caractere.isalpha():
        estado = 7
        
    elif estado == 7 and caractere.isalpha():
        estado = 7
        
    else:
        estado = -1  # Estado inválido

if  estado == 2 or estado == 3 or estado == 5 or estado == 7:
    print("Cadeia reconhecida")
    #print(estado)
    print(f"O token: " + token + " é um identificador")
else:
    print("Cadeia não reconhecida")
    #print(estado)
    print(token)
