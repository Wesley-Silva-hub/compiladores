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
    #token += caractere
    print(estado)
    if estado == 1:
        if caractere.isalpha():
            estado = 2
            token += caractere
        elif caractere == '<':
            estado = 8
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
        else:
            print(token)
            token = ""
            estado = 1
    
if estado in [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 28]:
    tokens.append(token)
    print(estado)
    print(tokens)
  
else:
    print("token nao formado")