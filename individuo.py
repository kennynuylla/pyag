import numpy.random as random, numpy as np, cromossomo

class Individuo: #Classe Base

    MUTACAO_PERTURBACAO = 0 #Algoritmo de Mutação Uniforme de Jeff Heaton - Artificial Intelligence for Humans - Vol. 2
    MUTACAO_PERTURBACAO_INT = 1
    MUTACAO_NOT = 2 #Not bit a bit
    MUTACAO_LISTA = 3 #Trocar Gene com base em uma lista

    TIPO_GENE_FLOAT = 0
    TIPO_GENE_INT = 1
    TIPO_GENE_BIN = 2

    CROSSOVER_ALTERNADO = 0 #Algoritmo de Ricardo Linden - Algoritmos Genéticos

    def __init__(self):
        self.cromossomos = []
        self.nota = None
        self.penalizacoes = 0
        self.id_penalizacoes = []

    def __repr__(self):
        return self.genes.__repr__()

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

    @classmethod
    def crossover(cls, ind1, ind2, tipo, argumento):
        filho1 = cls(argumento)
        filho2 = cls(argumento)

        cromossomos1 = []
        cromossomos2 = []

        for i in range(0, len(ind1.cromossomos)):

            cromossomo_ind_1 = ind1.cromossomos[i]
            cromossomo_ind_2 = ind2.cromossomos[i]
            cromossomo_filho_1 = cromossomo.Cromossomo(cromossomo_ind_1.tipo_mutacao, cromossomo_ind_1.valor_referencia_mutacao, cromossomo_ind_1.qtd_genes)
            cromossomo_filho_2 = cromossomo.Cromossomo(cromossomo_ind_1.tipo_mutacao, cromossomo_ind_1.valor_referencia_mutacao, cromossomo_ind_1.qtd_genes)

            if(tipo == cls.CROSSOVER_ALTERNADO):
                for e in range(0, len(cromossomo_ind_1.genes)):
                    if(random.uniform() > 0.5):
                        cromossomo_filho_1.genes.append(cromossomo_ind_1.genes[e])
                        cromossomo_filho_2.genes.append(cromossomo_ind_2.genes[e])
                    else:
                        cromossomo_filho_1.genes.append(cromossomo_ind_2.genes[e])
                        cromossomo_filho_2.genes.append(cromossomo_ind_1.genes[e])
            
            cromossomos1.append(cromossomo_filho_1)
            cromossomos2.append(cromossomo_filho_2)

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

if __name__ == "__main__":
    teste1 = Individuo()
    teste1.criar_cromossomo(Individuo.TIPO_GENE_FLOAT, 5, Individuo.MUTACAO_PERTURBACAO, 0.5, valores_maximos = [0.5, 0.7, 2, 0.6, 0.79])

    teste2 = Individuo()
    teste2.criar_cromossomo(Individuo.TIPO_GENE_FLOAT, 5, Individuo.MUTACAO_PERTURBACAO, 0.5, valores_maximos = [0.5, 0.7, 2, 0.6, 0.79])

    filho1, filho2 = Individuo.crossover(teste1, teste2, Individuo.CROSSOVER_ALTERNADO)

    print(teste1.cromossomos[0].genes)
    print(teste2.cromossomos[0].genes)
    print(filho1.cromossomos[0].genes)
    print(filho2.cromossomos[0].genes)