
lista = [10,8,3,15,4]

def ordena(listagem):
	i=0
	tamanho=len(listagem)
	while i<(tamanho-1):
		if listagem[i]>listagem[i+1]:
				listagem[i],listagem[i+1]=listagem[i+1],listagem[i]
		i+=1
	return listagem
ordena(lista)


#________________________________________________
#| Variável       | Tipo                        |
#|----------------|-----------------------------|
#| lista          | list[int](10,8,3,15,4)      |
#| tamanho        | int                         |
#| i              | int                         |
#|----------------|-----------------------------|
#1 variavel 16 bits
#3 variavel = 48 + 80 = 128
#lista cada variavel = 16 = 5 variaves -> 80
#____________________________________________________________________
#| Instrução                 |                                       |
#| ordena(lista)             |  função                               |
#| i<(tamanho-1)             | comparação                            |
#| listagem[i]>listagem[i+1] | comparação                            |
#| instrução                 | atribuição                            |
#| i+=1                      | ACRÉSCIMO (+1)                        |
#| return listagem           | retorno                               |
# --------------------------------------------------------------------
#1 instrução 16 bits
#6 instrução = 96

#TOTAL = 224

# prompt: como comentar multiplas linhas em python

# This is a single-line comment.

'''
This is a multi-line comment.
It can span multiple lines.
'''

"""
This is another way to write a multi-line comment.
It can also span multiple lines.
"""