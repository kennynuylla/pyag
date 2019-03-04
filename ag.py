import numpy as np, numpy.random as random, time, resultado, copy

class AG:

    PARADA_NGERACOES = 0
    PARADA_FITNESS = 1
    PARADA_NGERACOES_SEM_MELHORA = 2

    SELECAO_TORNEIO = 0

    OBJETIVO_SELECAO_CROSSOVER = 0
    OBJETIVO_SELECAO_MORTE = 1

    def __init__(self, classe_cromossomo, tamanho_populacao, argumento = None):
        self.classe_cromossomo = classe_cromossomo
        self.maximo_populacao = tamanho_populacao
        self.populacao = classe_cromossomo.gerar_aleatorio(tamanho_populacao, argumento)

        self.flag_configurado = False
        self.argumento = argumento

    def configurar(self, taxa_crossover, taxa_mutacao, tipo_crossover):
        self.taxa_crossover = taxa_crossover * self.maximo_populacao
        self.taxa_mutacao = taxa_mutacao * self.maximo_populacao
        self.tipo_crossover = tipo_crossover

        self.flag_configurado = True

    def checar_flags(self):
        if(self.flag_configurado == False):
            self.erro("Configure as taxas de Crossover e Mutação")

    def erro(self, mensagem):
        print(mensagem)
        exit(-1)

    def selecionar(self, tipo, objetivo):
        if(tipo == self.SELECAO_TORNEIO):
            if(objetivo == self.OBJETIVO_SELECAO_CROSSOVER):
                indices = random.randint(0, self.maximo_populacao, 4)
                ind1 = self.populacao[indices[0]]
                ind2 = self.populacao[indices[1]]
                ind3 = self.populacao[indices[2]]
                ind4 = self.populacao[indices[3]]

                retorno1 = None
                retorno2 = None

                if(ind1 > ind2):
                    retorno1 = ind1
                else:
                    retorno1 = ind2
                
                if(ind3 > ind4):
                    retorno2 = ind3
                else:
                    retorno2 = ind4

                return retorno1, retorno2
            else:
                indices = random.randint(0, self.maximo_populacao, 2)
                ind1 = self.populacao[indices[0]]
                ind2 = self.populacao[indices[1]]

                if(ind1 < ind2):
                    self.populacao.pop(indices[0])

                else:
                    self.populacao.pop(indices[1])

    def rodar(self, criterio_parada, valor_parada):
        self.checar_flags()
        geracao_atual = 1
        geracao_mudanca = 1
        tempo_inicio = time.time()
        acumulado_crossover = 0
        acumulado_mutacao = 0

        self.populacao.sort()
        melhor_individuo = copy.deepcopy(self.populacao[-1])

        #Variáveis para Gerar Resultados
        geracoes = []
        valores_fitness = []
        penalizacoes = []
        combos = []
        tempos = []

        while(True):
            if(criterio_parada == self.PARADA_NGERACOES):
                if(geracao_atual == valor_parada):
                    break
            elif(criterio_parada == self.PARADA_FITNESS):
                if(melhor_fitness == valor_parada):
                    break

            elif(criterio_parada == self.PARADA_NGERACOES_SEM_MELHORA):
                if(geracao_atual - geracao_mudanca == valor_parada):
                    break

            while(acumulado_crossover > 2):
                pai1,pai2 = self.selecionar(self.SELECAO_TORNEIO, self.OBJETIVO_SELECAO_CROSSOVER)
                filho1,filho2 = self.classe_cromossomo.crossover(pai1, pai2, self.tipo_crossover, self.argumento)
                filho1.avaliar()
                filho2.avaliar()

                if(filho1 > melhor_individuo):
                    geracao_mudanca = geracao_atual
                    melhor_individuo = copy.deepcopy(filho1)

                if(filho2 > melhor_individuo):
                    geracao_mudanca = geracao_atual
                    melhor_individuo = copy.deepcopy(filho2) 

                self.populacao.append(filho1)
                self.populacao.append(filho2)

                acumulado_crossover -= 2
            
            while(acumulado_mutacao > 1):
                indice = random.randint(0, self.maximo_populacao,1)[0]

                self.populacao[indice].mutar()
                self.populacao[indice].avaliar()

                if(self.populacao[indice] > melhor_individuo):
                    geracao_mudanca = geracao_atual
                    melhor_individuo = copy.deepcopy(self.populacao[indice])
                
                acumulado_mutacao -= 1

            while(len(self.populacao) > self.maximo_populacao):
                self.selecionar(self.SELECAO_TORNEIO, self.OBJETIVO_SELECAO_MORTE)

            combo = geracao_atual - geracao_mudanca
            tempo = time.time() - tempo_inicio

            print("Geração %d | Melhor Fitness: %.08f @ %d | Combo: %d" %(geracao_atual, melhor_individuo.nota, melhor_individuo.penalizacoes, combo))

            geracoes.append(geracao_atual)
            valores_fitness.append(melhor_individuo.nota)
            penalizacoes.append(melhor_individuo.penalizacoes)
            combos.append(combo)
            tempos.append(tempo)

            geracao_atual += 1

            acumulado_crossover += self.taxa_crossover
            acumulado_mutacao += self.taxa_mutacao
        
        return melhor_individuo, resultado.Resultado(geracoes, valores_fitness, penalizacoes, combos, tempos, melhor_individuo)

