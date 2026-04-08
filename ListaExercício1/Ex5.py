import random
random.seed(123)




#-------------------

# import random
# random.seed(123)

# def geraPastilha():
#     posPastilha = [1,2,3,4,5,6,7,8,9,10,11]
#     x = random.sample(posPastilha, 1)
#     y = random.sample(posPastilha, 1)
#     while(x==1 and y==1):
#         x = random.sample(posPastilha, 1)
#         y = random.sample(posPastilha, 1)
#     dicionario = {'x':x[0], 'y':y[0]}
#     return dicionario
    

# def move(prob, dicionario):
#     if prob<=25 and dicionario.get('x')>1:
#         dicionario['x'] = dicionario.get('x')-1
#     elif 25<prob<=50 and dicionario.get('y')<11:
#         dicionario['y']  = dicionario.get('y')+1
#     elif 50<prob<=75 and dicionario.get('x')<11:
#         dicionario['x']  = dicionario.get('x')+1
#     elif 75<prob<=100 and dicionario.get('y')>1:
#         dicionario['y']  = dicionario.get('y')-1

#     return dicionario


# def partidaPacMan():
#     posPacMan = {'x': 1, 'y': 1}
#     posF1 = {'x': 11, 'y': 1}
#     posF2 = {'x': 1, 'y': 11}
#     posF3 = {'x': 11, 'y': 11}

#     p1 = geraPastilha()
#     p2 = geraPastilha()
#     p3 = geraPastilha()
#     p4 = geraPastilha()

#     contPastilha = 4

#     while(contPastilha!=0):
#         if posPacMan.get('x') == 1 and posPacMan.get('y') == 1 :
#             probPacman = random.randint(50,100)
#         else: 
#             probPacman = random.randint(0,100)

#         posPacMan = move(probPacman, posPacMan)

#         if posPacMan == p1:
#             contPastilha -= 1
#         if posPacMan == p2:
#             contPastilha -= 1
#         if posPacMan == p3:
#             contPastilha -= 1
#         if posPacMan == p4:
#             contPastilha -= 1
        
#         probF1 = random.randint(0,100)
#         probF2 = random.randint(0,100)
#         probF3 = random.randint(0,100)

#         posF1 = move(probF1, posF1)
#         posF2 = move(probF2, posF2)
#         posF3 = move(probF3, posF3)

#         if posPacMan == posF1 or posPacMan == posF2 or posPacMan == posF3:
#             return False
        
#     return True

# dicionario_partida = {'vencedor': 0, 'perdedor': 0}
# for i in range(1000):
#     resultado = partidaPacMan()
#     if resultado:
#         dicionario_partida['vencedor'] = dicionario_partida.get('vencedor') +1
#     else:
#         dicionario_partida['perdedor'] = dicionario_partida.get('perdedor') +1

# print(dicionario_partida.get('vencedor'))
# print(dicionario_partida.get('perdedor'))

# print(f"Probabilidade de vitoria: {dicionario_partida.get('vencedor')/1000}")