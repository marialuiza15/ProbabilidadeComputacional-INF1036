import numpy as np

c =2
alvo = 10000 #aceitas

amostra_de_aceitas =[]
tentativas_totais = 0

while len(amostra_de_aceitas)<alvo:
    u1 =np.random.uniform(0,1)
    u2 = np.random.uniform(0,1)  

    tentativas_totais+=1

    pu1 = 2*u1 #altura da curva

    r = pu1/c #razao

    if u2<=r: #verificando se o ponto u2 é nmenor ou igual ao ponto u1
        amostra_de_aceitas.append(u1)


qtd_aceito = len(amostra_de_aceitas)
qtd_rejeitado = tentativas_totais- qtd_aceito

print("Aceitos: ",qtd_aceito)
print("Rejeitados: ",qtd_rejeitado)