import sistema, sys

sys.path.append("./../")

import ag

motor = ag.AG(sistema.Sistema, 400)
motor.configurar(0.85, 0.1, sistema.Sistema.CROSSOVER_ALTERNADO)
campeao, resultados = motor.rodar(ag.AG.PARADA_NGERACOES_SEM_MELHORA, 200)

resultados.plotar_fitness_x_geracoes()
resultados.plotar_fitness_x_tempo()
resultados.plotar_combos_x_geracoes()
resultados.gerar_relatorio()