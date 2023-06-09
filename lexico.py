arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
token = ""
estado = 1
tokens = []
palavras_reservadas = ["if", "else", "then", "while", "for", "switch", "case", "break", "continue", "return", "def", "class", "import", "from", "as", "try", "except", "finally", "raise", "assert", "global", "True", "False"]
digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", "~", "`"]

#FALTA REFAZER O AUTOMATO PARA SO UM GRANDAO E VER OS ESTADOS FINAIS



for i in range(len(conteudo)):
    caractere = conteudo[i]

    
    if estado == -1:
        estado = 1
   
    
    token += caractere
    if estado == 1 and caractere.isalpha():
        estado = 2
        
    elif caractere == '_' and estado == 2:
        estado = 4
    
    elif caractere == '.' and estado == 2:
        estado = 6

    elif caractere.isalpha() and estado == 2:
        estado = 3
        
    elif (caractere.isalpha() or caractere.isnumeric()) and estado == 3:
        estado = 3

    elif estado == 4 and (caractere.isalpha() or caractere.isnumeric()):
        estado = 5

    elif (caractere.isalpha() or caractere.isnumeric()) and estado == 5:
        estado = 5
        
    elif caractere.isalpha() and estado == 6:
        estado = 7
        
    elif caractere.isalpha() and estado == 7:
        estado = 7
        
    else:
        if estado == 2 or estado == 3 or estado == 5 or estado == 7:
            tokens.append(token)
            token = ""
        else:
            estado = -1  # Definir estado como -1 quando nenhuma condição é atendida
if estado == 2 or estado == 3 or estado == 5 or estado == 7:
    if token != "":
        tokens.append(token)
    #print("Cadeia reconhecida")
else:
    if estado == -1:
        #    tokens.append(token)
        #token = ""
        #estado = -1  # Definir estado como -1 quando nenhuma condição é atendida
        print("token invalido")


for token in tokens:
    token = token.strip()
    if token in palavras_reservadas:
        print("PL: " + token)
    elif token in simbolos:
        print("SIMBOLO: " + token)
    elif token in digitos:
        print("DIGITO: " + token)
    else:
        print("ID: " + token)
