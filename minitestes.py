estado =1
caractere = '%'

simbolos_outros = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '=', '`', '~', '[', ']', '{', '}', '|', '\\', ':', ';', "'", '"', ',', '.', '/', '?']



if estado == 1 and caractere in simbolos_outros:
        print(caractere)