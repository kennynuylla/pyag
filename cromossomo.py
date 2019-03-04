import numpy.random as random, numpy as np

class Cromossomo:

    MUTACAO_PERTURBACAO = 0 #Algoritmo de Mutação Uniforme de Jeff Heaton - Artificial Intelligence for Humans - Vol. 2
    MUTACAO_PERTURBACAO_INT = 1
    MUTACAO_NOT = 2 #Not bit a bit
    MUTACAO_LISTA = 3 #Trocar Gene com base em uma lista

    TIPO_GENE_FLOAT = 0
    TIPO_GENE_INT = 1
    TIPO_GENE_BIN = 2

    def __init__(self, tipo_mutacao, valor_referencia_mutacao, qtd_genes):
        self.qtd_genes = 0
        self.tipo_mutacao = tipo_mutacao
        self.valor_referencia_mutacao = valor_referencia_mutacao
        self.qtd_genes = qtd_genes
        self.genes = []

    def mutar(self):
        if(self.tipo_mutacao == self.MUTACAO_PERTURBACAO):
            alteracao = random.uniform(-self.valor_referencia_mutacao, self.valor_referencia_mutacao, self.qtd_genes)
            self.genes *= 1+alteracao

        elif(self.tipo_mutacao == self.MUTACAO_PERTURBACAO_INT):
            for i in range(0, self.qtd_genes):
                alteracao = random.randint(self.valor_referencia_mutacao[0], self.valor_referencia_mutacao[1])
                self.genes[i] += alteracao

    @classmethod
    def aleatorio(cls, tipo, qtd_genes, tipo_mutacao, valor_referencia_mutacao, valores_minimos, valores_maximos):
        cromo = cls(tipo_mutacao, valor_referencia_mutacao, qtd_genes)

        if(tipo == cls.TIPO_GENE_FLOAT):
            cromo.genes = random.uniform(size = qtd_genes)

            for i in range(0, qtd_genes):
                if(valores_minimos == None):
                    valor_minimo = 0
                else:
                    valor_minimo = valores_minimos[i]

                if(valores_maximos == None):
                    valor_maximo = 1
                
                else:
                    valor_maximo = valores_maximos[i]

                #Algoritmo de Desnormalização de Jeff Heaton - Artificial Intelligence for Humans - Vol. 1

                amplitude = valor_maximo - valor_minimo

                cromo.genes[i] = valor_minimo + cromo.genes[i] * amplitude

        if(tipo == cls.TIPO_GENE_INT):
            for i in range(0, qtd_genes):
                if(valores_minimos == None):
                    valor_minimo = 0 
                else:
                    valor_minimo = valores_minimos[i]

                if(valores_maximos == None):
                    valor_maximo = 2
                else:
                    valor_maximo = valores_maximos[i]
                
                cromo.genes.append(random.randint(valor_minimo, valor_maximo))

        return cromo