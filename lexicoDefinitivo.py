arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
token = ""
pl = ""
id = ""
digito = ""
simbolo = ""
contador = 1
contador_linha = 1
estado = 1
tokens = []
conteudo_modificado = ""
simbolos_outros = ["!", "#", "$", "%", "(", ")", "=", "{", "}", "[", "]", "|", ":", ";", "'", "\"", ">", ",", ".", "?", "~", "`"]
palavras_reservadas = ["program", "if", "else", "then", "while", "do", "until", "repeat", "int", "double", "char", "case", "switch", "end", "procedure", "function", "bengin", "for"]
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ['!', '"', '#', '$', '%', "'", '(', ')', '+', ',', '-', '.', ':', ';', '<', '=', '>', '?', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

ult_caractere_espaco = False 

for i in range(len(conteudo)):
    ult_caractere_espaco = False 
    caractere = conteudo[i]   


    if caractere == '\n':
        contador_linha += 1

    if caractere == ' ' or caractere == '\n' or caractere == '\t':
        if ult_caractere_espaco:
            estado = 1
            continue

        ult_caractere_espaco = True
        if token != '':
            tokens.append(token)
            token = ""
            continue
        
        

    ult_caractere_espaco = False
    

    if estado == 1:
        if caractere.isalpha():
            estado = 2
            token += caractere
        elif caractere == '<':
            estado = 8
            token += caractere
        elif caractere == '+':
            estado = 10
            token += caractere
        elif caractere == '-':
            estado = 12
            token += caractere
        elif caractere in simbolos:
            token += caractere
            tokens.append(token)
            token = ""
            continue
        elif caractere == '>':
            estado = 14
            token += caractere
        elif caractere.isnumeric():
            estado = 17
            token += caractere
        elif caractere == '@':
            estado = 20
            token += caractere
        elif caractere == '*':
            estado = 21
            token += caractere
        elif caractere == '/':
            estado = 25
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 2:
        if caractere == '_':
                estado = 4
                token += caractere
        elif caractere == '.':
            estado = 6
            token += caractere
        elif caractere.isalpha():
            estado = 3
            token += caractere
        else:
            print(token)
            tokens.append(token)
            token = ''
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1

    elif estado == 3:
        if caractere.isalpha():
            estado = 3
            token += caractere
        elif caractere == '_':
                estado = 3
                token += caractere
        else:
            print(token)
            token += caractere
            tokens.append(token)
            token = ""
           
            
            
            estado = 1
    elif estado == 4:
        if caractere.isalpha():
            estado = 5
            token += caractere
        else:
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 5:
        if caractere.isalpha():
            estado = 5
            token += caractere
        else: 
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 6:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 7:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 7:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 8:
        if caractere == '>':
            estado = 9
            token += caractere
        elif caractere == '=':
            estado = 9
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 10:
        if caractere == '+':
            estado = 11
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 12:
        if caractere.isnumeric():
            estado = 17
            token += caractere
        elif caractere.isdigit():
            estado = 17
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 14:
        if caractere == '=':
            estado = 13
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
            estado = ''
    elif estado == 17:
        if caractere.isnumeric():
            estado = 17
            token += caractere
        elif caractere == ',':
            estado = 16
            token += caractere

        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 17:
        if caractere == ',':
            estado = 16
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1

    elif estado == 18:
        if caractere == '\n':
            estado = 18
        elif caractere.isalpha() or caractere.isnumeric or caractere.isnum():
            token += caractere
            estado = 1
        else:
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1

    elif estado == 16:
        if caractere.isnumeric():
            estado = 15
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 15:
        if caractere.isnumeric():
            estado = 15 
            token += caractere
        else:
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 20:
        if caractere == '@':
            estado = 19
            token += caractere
        else:
           
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 19:
        if caractere == '\n':
            estado = 18
            token += caractere
        elif caractere.isalpha() or caractere.isnumeric or caractere.isnum():
            estado = 18
            token += caractere
        else:
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 21:
        if caractere == '*':
            estado = 22
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 22:
        if caractere in simbolos_outros:
            estado = 22
            token += caractere
        elif caractere == '*':
            estado = 23
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 23:
        if caractere == '*':
            estado = 24
            token += caractere
        elif caractere in simbolos_outros:
            estado = 22
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 24:
        if caractere == '*':
            estado = 24
        else:
            print(token)
            tokens.append(token)
            token += caractere
            
            estado = 1

    elif estado == 25:
        if caractere == '/':
            estado = 26
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 26:
        if caractere == '/':
            estado = 27
            token += caractere
        if caractere in simbolos_outros:
            estado = 26
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
    elif estado == 27:
        if caractere == '/':
            estado = 28
            token += caractere
        elif caractere in simbolos_outros:
            estado = 26
            token += caractere
        else:
            if caractere == "\n" or ' ':
                continue
            print(token)
            tokens.append(token)
            token = ""
            token += caractere
            tokens.append(token)
            token = ""
            estado = 1
        

if estado in [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 28]:
    tokens.append(token)
    #print(estado)
    #print(tokens)
  
else:

    print(f"Erro na linha {contador_linha}")
    #token += caractere
    #tokens.append(token)
print(tokens)


for token in tokens:
    if token in palavras_reservadas:  
        print(f"PL: {token}")
    elif token in simbolos:  
        print(f"SIMBOLO: {token}")
    elif token.startswith('-') or token.isdigit():
        print(f"DIGITO: {token}")
    else:     
        print(f"ID: {token}")