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

#ultima versao do lexico

for i in range(len(conteudo)):
    
    #if estado == -1:
        #tokens.append(token)
        #token = ''
     #  estado = 1
     #   continue
    #if  estado == 0:
     #   estado = 1
        #tentar fazer uma funcao para cada automato ou 
    caractere = conteudo[i]
    #token += caractere
    print(estado)
    if estado == 1 and caractere.isalpha():
        estado = 2   
        #token += caractere
    elif estado == 2 and caractere.isalpha():
        estado = 3
        #token += caractere
    elif estado == 3 and caractere.isalpha():
        estado = 3
        #token += caractere
    elif estado == 2 and caractere == '_':
        estado = 4
        #token += caractere
    elif estado == 4 and caractere.isalpha():
        estado = 5
        #token += caractere
    elif estado == 5 and caractere.isalpha():
        estado = 5
        #token += caractere
    elif estado == 2 and caractere == '.':
        estado = 6
        #token += caractere
    elif estado == 6 and caractere.isalpha():
        estado = 7
        #token += caractere
    elif estado == 7 and caractere.isalpha():
        estado = 7
        #token += caractere
    elif estado == 1 and caractere == '<':
        estado = 8
        #token += caractere
    elif estado == 8 and caractere == '>':
        estado = 9
        #token += caractere
    elif estado == 8 and caractere == '=':
        estado = 9
        #token += caractere
    elif estado == 1 and caractere == '+':
        estado = 10
        #token += caractere
    elif estado == 10 and caractere == '+':
        estado = 11
        #token += caractere
    elif estado == 1 and caractere == '-':
        estado = 12
        #token += caractere
    elif estado == 12 and caractere.isnumeric():
        estado = 17
        #token += caractere
    elif estado == 1 and caractere in simbolos_outros:
        estado = 13
        #token += caractere
    elif estado == 1 and caractere == '>':
        estado = 14
        #token += caractere
    elif estado == 14 and caractere == '=':
        estado = 13
        #token += caractere
    elif estado == 1 and caractere == ':':
        estado = 14
        #token += caractere
    elif estado == 14 and caractere == '=':
        estado = 13
        #token += caractere
    elif estado == 1 and caractere.isnumeric():
        estado = 17
        #token += caractere
    elif estado == 17 and caractere.isnumeric():
        estado = 17
        #token += caractere
    elif estado == 17 and caractere == ',':
        estado = 16
        #token += caractere
    elif estado == 16 and caractere.isnumeric():
        estado = 15
        #token += caractere
    elif estado == 15 and caractere.isnumeric():
        estado = 15
        #token += caractere
    elif estado == 1 and caractere == '@':
        estado = 20
        #token += caractere
    elif estado == 20 and caractere == '@':
        estado = 19
        #token += caractere
    elif estado == 19 and  caractere == '\n':
        estado = 18
        #token += caractere
    elif estado == 1 and caractere == '*':
        estado = 21
        #token += caractere
    elif estado == 21 and caractere == '*':
        estado = 22
        #token += caractere
    elif estado == 22 and caractere in simbolos:
        estado = 22
        #token += caractere
    elif estado == 22 and caractere == '*':
        estado = 23
        #token += caractere
    elif estado == 23 and caractere in simbolos:
        estado = 22
        #token += caractere
    elif estado == 23 and caractere == '*':
        estado = 24
        #token += caractere
    elif estado == 1 and caractere == '/':
        estado = 25
        #token += caractere
    elif estado == 25 and caractere == '/':
        estado = 26
        #token += caractere
    elif estado == 26 and caractere in simbolos:
        estado = 26
        #token += caractere
    elif estado == 26 and caractere == '/':
        estado = 27
        #token += caractere
    elif estado == 27 and caractere in simbolos:
        estado = 26
        #token += caractere
    elif estado == 27 and caractere == '/':
        estado = 28
        #token += caractere
    
    token += caractere



#ideia do alex blenda
#if estado == 1
   # if simbolo.isalpha()
     #   estado = 2
     #   token += simbolo
   # elif simbolo == !
     #   estado = 23
     #   token += simbolo
  #  else
        
#elif outro_estado
   # if simbolo
...

    
if estado in [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 28]:
    tokens.append(token)
    token = ''
    print(estado)
    print(tokens)
  
else:
    print(tokens)
    print(estado)
    print("token nao formado")