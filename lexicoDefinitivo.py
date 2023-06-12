arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
token = ""
estado = 1
tokens = []
conteudo_modificado = ""
simbolos_outros = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '=', '`', '~', '[', ']', '{', '}', '|', '\\', ':', ';', "'", '"', ',', '.', '?']
palavras_reservadas = ["if", "else", "then", "while", "for", "switch", "case", "break", "continue", "return", "def", "class", "import", "from", "as", "try", "except", "finally", "raise", "assert", "global", "True", "False"]
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", "~", "`"]


for i in range(len(conteudo)):
    
    caractere = conteudo[i]
    print(estado)
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
            estado = 13
            token += caractere
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
            print(token)
            estado = 1
            token = ""
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
            estado = 1
            token = ""
    elif estado == 3:
        if caractere.isalpha():
            estado = 3
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 4:
        if caractere.isalpha():
            estado = 5
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 5:
        if caractere.isalpha():
            estado = 5
            token += caractere
        else: 
            print(token)
            token = ""
            estado = 1
    elif estado == 6:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 7:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 7:
        if caractere.isalpha():
            estado = 7
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 8:
        if caractere == '>':
            estado = 9
            token += caractere
        elif caractere == '=':
            estado = 9
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 10:
        if caractere == '+':
            estado = 11
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 12:
        if caractere.isnumeric():
            estado = 17
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 14:
        if caractere == '=':
            estado = 13
            token += caractere
        else:
            print(token)
            token = ""
            estado = ''
    elif estado == 17:
        if caractere.isnumeric():
            estado = 17
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 17:
        if caractere == ',':
            estado = 16
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 16:
        if caractere.isnumeric():
            estado = 15
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 15:
        if caractere.isnumeric():
            estado = 15 
            token += caractere
        else:
            print(token)
            token = ""
            estado = 1
    elif estado == 20:
        if caractere == '@':
            estado = 19
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 19:
        if caractere == '\n':
            estado = 18
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 21:
        if caractere == '*':
            estado = 22
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 22:
        if caractere in simbolos:
            estado = 22
            token += caractere
        elif caractere == '*':
            estado = 23
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 23:
        if caractere == '*':
            estado = 24
            token += caractere
        elif caractere in simbolos:
            estado = 22
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 25:
        if caractere == '/':
            estado = 26
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 26:
        if caractere == '/':
            estado = 27
            token += caractere
        if caractere in simbolos:
            estado = 26
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1
    elif estado == 27:
        if caractere == '/':
            estado = 28
            token += caractere
        elif caractere in simbolos:
            estado = 26
            token += caractere
        else:
            print(token)
            token = ''
            estado = 1

if estado in [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 28]:
    tokens.append(token)
    #print(estado)
    print(tokens)
  
else:
    print(estado)
    print("token nao formado")

#print(tokens)