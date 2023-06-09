arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
string = ""
simbolos_outros = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '=', '`', '~', '[', ']', '{', '}', '|', '\\', ':', ';', "'", '"', ',', '.', '?']
palavras_reservadas = ["if", "else", "then", "while", "for", "switch", "case", "break", "continue", "return", "def", "class", "import", "from", "as", "try", "except", "finally", "raise", "assert", "global", "True", "False"]
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", "~", "`"]


for i in range(len(conteudo)):
    string += conteudo[i]



def automato_identificador(string):
    identificador = ""
    estado = 1

    for i in range(len(string)):
        caractere = conteudo[i]

        if estado == 1 and caractere.isalpha():
            estado = 2   
        elif estado == 2 and caractere.isalpha():
            estado = 3
        elif estado == 3 and caractere.isalpha():
            estado = 3
        elif estado == 2 and caractere == '_':
            estado = 4
        elif estado == 4 and caractere.isalpha():
            estado = 5
        elif estado == 5 and caractere.isalpha():
            estado = 5
        elif estado == 2 and caractere == '.':
            estado = 6
        elif estado == 6 and caractere.isalpha():
            estado = 7
        elif estado == 7 and caractere.isalpha():
            estado = 7
        else: 
            estado = -1
        identificador += caractere

    if  estado == 2 or estado == 3 or estado == 5 or estado == 7:
        print(estado)
        #identificador.append(token)
        print(identificador)
        #identificador = ""
        return identificador

    else:
        return print("token nao formado")

def automato_simbolo(string):
    simbolo = ""
    caractere = conteudo[i]

    if estado == 1 and caractere == '<':
        estado = 8
    elif estado == 8 and caractere == '>':
        estado = 9  
    elif estado == 8 and caractere == '=':
        estado = 9
    elif estado == 1 and caractere == '+':
        estado = 10
    elif estado == 10 and caractere == '+':
        estado = 11
    elif estado == 1 and caractere == '-':
        estado = 12
    elif estado == 1 and caractere in simbolos_outros:
        estado = 13
    elif estado == 1 and caractere == '>':
        estado = 14
    elif estado == 14 and caractere == '=':
        estado = 13
    elif estado == 1 and caractere == ':':
        estado = 14
    elif estado == 14 and caractere == '=':
        estado = 13
    simbolo += caractere
    if  estado == 8 or estado == 9 or estado == 10 or estado == 11 or estado == 12 or estado == 13 or estado == 14:
        return simbolo
    else:
        print("token nao formado")
    



automato_identificador(string)
        
    