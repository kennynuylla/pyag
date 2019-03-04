import numpy as np, matplotlib.pyplot as plt 

class Resultado:

    def __init__(self, geracoes, valores_fitness, penalizacoes, combos, tempos, campeao):
        self.geracoes = geracoes
        self.valores_fitness = valores_fitness
        self.penalizacoes = penalizacoes
        self.combos = combos
        self.tempos = tempos
        self.campeao = campeao

    def plotar_fitness_x_geracoes(self):
        plt.subplot(2,1,1)
        plt.title("Melhor Indivíduo ao Longo das Gerações")
        plt.ylabel("Melhor Fitness")
        plt.grid(True)
        plt.plot(self.geracoes, self.valores_fitness, "b-")

        plt.subplot(2,1,2)
        plt.xlabel("Geração")
        plt.ylabel("Melhor Número de Penalizações")
        plt.ylim(0, 5)
        plt.grid()
        plt.plot(self.geracoes, self.penalizacoes, "r-")
        plt.show()

    def plotar_fitness_x_tempo(self):
        plt.title("Melhor Fitness ao Longo do Tempo de Execução")
        plt.xlabel("Tempo de Execução [s]")
        plt.ylabel("Melhor Fitness")
        plt.grid(True)
        plt.plot(self.tempos, self.valores_fitness, "g-")
        plt.show()

    def plotar_combos_x_geracoes(self):
        plt.title("Combos ao Longo das Gerações")
        plt.xlabel("Geração")
        plt.ylabel("Combo")
        plt.grid(True)
        plt.plot(self.geracoes, self.combos, "k-")
        plt.show()

    def gerar_relatorio_detalhadado(self, arquivo = "relatorio.txt"):
        relatorio = open(arquivo, "w")
        for i in range(0, len(self.geracoes)):
            linha = "Geração: %d | Melhor Fitness: %.04f | Melhor Penalizações: %d | Tempo de Execução: %.04f [s]\n" %(
                self.geracoes[i], self.valores_fitness[i], self.penalizacoes[i], self.tempos[i]
            )
            relatorio.write(linha)
        relatorio.close()

    def gerar_relatorio(self, arquivo="relatorio.txt"):
        relatorio = open(arquivo, "w")
        relatorio.write(".:Dados do Melhor Indivíduo\n")
        relatorio.write("%s\n\n" %(self.campeao))
        relatorio.write(".:Dados de Execução\n")
        relatorio.write("%d Gerações | %.04f s de execução" %(self.geracoes[-1], self.tempos[-1]))
        relatorio.close()
