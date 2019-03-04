import numpy.random as random, numpy as np, cromossomo, copy

class Individuo: #Classe Base

    MUTACAO_PERTURBACAO = 0 #Algoritmo de Mutação Uniforme de Jeff Heaton - Artificial Intelligence for Humans - Vol. 2
    MUTACAO_PERTURBACAO_INT = 1
    MUTACAO_NOT = 2 #Not bit a bit
    MUTACAO_LISTA = 3 #Trocar Gene com base em uma lista

    TIPO_GENE_FLOAT = 0
    TIPO_GENE_INT = 1
    TIPO_GENE_BIN = 2

    CROSSOVER_ALTERNADO = 0 #Algoritmo de Ricardo Linden - Algoritmos Genéticos

    def __init__(self, argumento = None):
        self.cromossomos = []
        self.nota = None
        self.penalizacoes = 0
        self.id_penalizacoes = []

    def __lt__(self,outro):
        return not(self.__ge__(outro))

    def __ne__(self,outro):
        return not(self.__eq__(outro))

    def __ge__(self,outro):
        return (self.__gt__(outro) or self.__eq__(outro))

    def __le__(self,outro):
        return (self.__lt__(outro) or self.__eq__(outro))

    def __eq__(self, outro):
        for i in range(0, len(self.cromossomos)):
            for e in range(0, len(self.cromossomos[i].genes)):
                if(self.cromossomos[i].genes[e] != outro.cromossomos[i].genes[e]):
                    return False
        return True

    def __str__(self):
        linha = "Fitness: %f\nPenalizações: %d\n-------------------\n" %(self.nota, self.penalizacoes)
        for i in range(0, len(self.id_penalizacoes)):
            linha += "%s\n" %(self.id_penalizacoes[i])    
        linha += "---------------------------\nGenes:\n---------------------------\n"
        for i in range(0, len(self.cromossomos)):
            linha += "Cromossomo %d: " %(i+1)
            for e in range(0, len(self.cromossomos[i].genes)):
                linha += "%f " %(self.cromossomos[i].genes[e])
            linha += "\n"
        return linha

    def criar_cromossomo(self, tipo, qtd_genes, tipo_mutacao, valor_referencia_mutacao, valores_minimos = None, valores_maximos = None):
        self.cromossomos.append(cromossomo.Cromossomo.aleatorio(tipo, qtd_genes, tipo_mutacao, valor_referencia_mutacao, valores_minimos, valores_maximos))

    def mutar(self):
        for cromossomo in self.cromossomos:
            cromossomo.mutar()

    def avaliar(self):
        self.nota = None
        self.penalizacoes = 0
        self.id_penalizacoes = []


    #Essas funções serão chamadas através classe herdeira
    @classmethod
    def crossover(cls, ind1, ind2, tipo, argumento):
        filho1 = cls(argumento) #A classe herdeira recebe um segundo parâmetro, que é o argumento
        filho2 = cls(argumento)

        cromossomos1 = []
        cromossomos2 = []

        for i in range(0, len(ind1.cromossomos)):

            cromossomo_ind_1 = ind1.cromossomos[i]
            cromossomo_ind_2 = ind2.cromossomos[i]

            #Cria cromossomos vazios com as mesma configurações dos cromossomso dos pais
            cromossomo_filho_1 = copy.deepcopy(cromossomo_ind_1) #deepcopy para garantir que não vá nenhuma referência
            cromossomo_filho_2 = copy.deepcopy(cromossomo_ind_2)

            if(tipo == cls.CROSSOVER_ALTERNADO):
                for e in range(0, len(cromossomo_ind_1.genes)):
                    if(random.uniform() < 0.5): #50% de chances de inverter
                        cromossomo_filho_1.genes[e] = copy.deepcopy(cromossomo_ind_2.genes[e])
                        cromossomo_filho_2.genes[e] = copy.deepcopy(cromossomo_ind_1.genes[e])
            
            cromossomos1.append(copy.deepcopy(cromossomo_filho_1))
            cromossomos2.append(copy.deepcopy(cromossomo_filho_2))

        filho1.cromossomos = cromossomos1
        filho2.cromossomos = cromossomos2

        return filho1, filho2

    @classmethod
    def gerar_aleatorio(cls, quantidade, argumento):
        retorno = []

        for i in range(quantidade):
            temp = cls(argumento)
            temp.avaliar()
            retorno.append(temp)

        return retorno