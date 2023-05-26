#IMPLEMENTACAO DO LEXICO

arquivo = open('/home/josewesley/projetos/compiladores/entrada.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

for i in range(len(conteudo)):
    caractere = conteudo[i]
    print(caractere)
        
        