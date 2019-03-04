import sys

sys.path.append("./../")

import individuo, numpy as np

class Sistema(individuo.Individuo):

    def __init__(self, argumento):
        super().__init__()
        self.criar_cromossomo(self.TIPO_GENE_FLOAT, 3, self.MUTACAO_PERTURBACAO, 0.01, [-1,-1,-1], [1,1,1])

    def avaliar(self):
        super().avaliar()
        x = self.cromossomos[0].genes[0]
        y = self.cromossomos[0].genes[1]
        z = self.cromossomos[0].genes[2]

        self.nota = 10*(x-y**2)**2 +2*np.sin(x) + z*np.exp(-z) + y**2 * np.sin(y)

        if(not(x>y)):
            self.penalizacoes += 1
        
        if(not(y**2 + z**2 > 0.3)):
            self.penalizacoes += 1

        if(not(abs(x) <= 1 and abs(y) <= 1 and abs(z) <= 1)):
            self.penalizacoes += 1

    def __gt__(self, outro):
        if (self.penalizacoes > outro.penalizacoes):
            return False
        
        if (self.penalizacoes == outro.penalizacoes):
            return self.nota > outro.nota
        
        return True

    