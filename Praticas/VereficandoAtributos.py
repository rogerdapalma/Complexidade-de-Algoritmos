#CODIGO RETIRADO DO GITHUB DO PROFESSOR ALEXANDRE ZAMBERLAN
#https://github.com/alexandrezamberlan/pesquisa_ordenacao/blob/master/03-ordenacao/Python/ordenacao.py


class Ordenacao:
    @staticmethod
    def bolha(lista):
        houveTroca = True
        while (houveTroca):
            houveTroca = False
            for i in range(0, len(lista) - 1):
                if (lista[i] > lista[i+1]):
                    houveTroca = True
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp

    @staticmethod
    def selecao(lista):       
        for i in range(0, len(lista) -1):
            posMenor = i
            for j in range(i+1, len(lista)):
                if (lista[j] < lista[posMenor]):
                    posMenor = j

            if (i != posMenor):
                tmp = lista[i]
                lista[i] = lista[posMenor]
                lista[posMenor] = tmp

    @staticmethod
    def insercao(lista):   
        for i in range(1, len(lista)):
            tmp = lista[i]
            j = i - 1
            while (j >= 0):
                if (tmp < lista[j]):
                    lista[j + 1] = lista[j]
                else: 
                    break
                j -= 1

            lista[j + 1] = tmp

    @staticmethod
    def pente(lista):
        distancia = len(lista)

        houveTroca = True
        while (houveTroca and distancia > 1):
            distancia = int(distancia / 1.3)
            if (distancia < 1):
                distancia = 1
            houveTroca = False
            for i in range(0, len(lista) - distancia):
                if (lista[i] > lista[i+distancia]):
                    houveTroca = True
                    tmp = lista[i]
                    lista[i] = lista[i+distancia]
                    lista[i+distancia] = tmp


    @staticmethod
    def shell(lista):   
        distancia = 1
        referenciaTamanho = 3

        while (distancia < len(lista)):
            distancia = referenciaTamanho * distancia + 1


        while (distancia > 1):
            distancia = int(float(distancia / referenciaTamanho))

            for i in range(distancia, len(lista)):
                tmp = lista[i]
                j = i - distancia
                while (j >= 0): 
                    if (tmp < lista[j]):
                        lista[j + distancia] = lista[j]                    
                    else:
                        break
                    j = j - distancia

                lista[j + distancia] = tmp


    def particiona(lista, ini, fim):
        pivo = ini
        while (fim > ini):
            while (fim > pivo and lista[fim] > lista[pivo]):
                fim -= 1

            if (fim > pivo):
                tmp = lista[pivo]
                lista[pivo] = lista[fim]
                lista[fim] = tmp
                pivo = fim

            ini += 1
            while (ini < pivo and lista[ini] < lista[pivo]):
                ini += 1

            if (ini < pivo):
                tmp = lista[pivo]
                lista[pivo] = lista[ini]
                lista[ini] = tmp
                pivo = ini

        return pivo

    @staticmethod
    def quick(lista, ini, fim):
        pivo = particiona(lista, ini, fim)

        if (ini < pivo - 1):
            quick(lista, ini, pivo - 1)
        if (pivo + 1 < fim):
            quick(vetor, pivo + 1, fim)
          # ______________________________________
          #| Variável            | Tipo           |
          #|---------------------|----------------|
          #| lista               | list           |
          #| houveTroca          | bool           |
          #| i                   | int            |
          #| j                   | int            |
          #| posMenor            | int            |
          #| tmp                 | int            |
          #| distancia           | int            |
          #| referenciaTamanho   | int            |
          #| pivo                | int            |
          #| ini                 | int            |
          #| fim                 | int            |
          #| Instrução           | atribuição     |
          #|                     | adição         |
          #|                     | subtração      |
          #|                     | multiplicação  |
          #|                     | divisão        |
          #|                     | chamada de função |
          #|                     | comparação     |
          #|                     | troca de valor |
          #|                     | retorno        |
          # ---------------------------------------