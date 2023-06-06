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

def lexico(caractere):
        
        estado = 1
        token = ""
        token += caractere

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
        elif estado == 1 and caractere == '<':
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
        elif estado == 12 and caractere.isnumeric():
            estado = 17
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
        elif estado == 1 and caractere.isnumeric():
            estado = 17
        elif estado == 17 and caractere.isnumeric():
            estado = 17
        elif estado == 17 and caractere == ',':
            estado = 16
        elif estado == 16 and caractere.isnumeric():
            estado = 15
        elif estado == 15 and caractere.isnumeric():
            estado = 15
        elif estado == 1 and caractere == '@':
            estado = 20
        elif estado == 20 and caractere == '@':
            estado = 19
        elif estado == 19 and  caractere == '\n':
            estado = 18
        elif estado == 1 and caractere == '*':
            estado = 21
        elif estado == 21 and caractere == '*':
            estado = 22
        elif estado == 22 and caractere in simbolos:
            estado = 22
        elif estado == 22 and caractere == '*':
            estado = 23
        elif estado == 23 and caractere in simbolos:
            estado = 22
        elif estado == 23 and caractere == '*':
            estado = 24
        elif estado == 1 and caractere == '/':
            estado = 25
        elif estado == 25 and caractere == '/':
            estado = 26
        elif estado == 26 and caractere in simbolos:
            estado = 26
        elif estado == 26 and caractere == '/':
            estado = 27
        elif estado == 27 and caractere in simbolos:
            estado = 26
        elif estado == 27 and caractere == '/':
            estado = 28
        
        if estado in [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 28]:
            print(estado)
            return tokens.append(token)
        else:
            print(estado)
            print("token nao formado")

for i in range(len(conteudo)):

    caractere = conteudo[i]
    

    if caractere == ' ' or '\n':
        continue

    lexico(caractere)