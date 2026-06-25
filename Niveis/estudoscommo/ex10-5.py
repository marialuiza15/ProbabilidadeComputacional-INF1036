import numpy as np

tempo_max = 480
tempo_atual = 0


qtd_total = 0
fila=0

banheiro_ocupado_por = 0
while tempo_atual<tempo_max:
        tempo_chegada_na_fila = np.random.exponential(4)

        tempo_atual += tempo_chegada_na_fila #avança o tempo ate o momento da pessao chegar
        
        qtd_total+=1

        tempo_uso = np.random.exponential(3)

        if tempo_uso<tempo_chegada_na_fila:
            fila+=1
            banheiro_ocupado_por+= tempo_uso
        else:
            banheiro_ocupado_por = tempo_uso + tempo_atual

print(qtd_total)
print(fila)
        