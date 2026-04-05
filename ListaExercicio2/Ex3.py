import random
random.seed(123)

def proxPartindoEstado1(lista, l_cont):
    prob = random.random()

    if prob<=0.6:
        lista[0] = 1 #estado 1
        lista[1] = 0
        lista[2] = 0

        l_cont[0]+=1

    elif 0.6<prob<=0.9:
        lista[0] = 0
        lista[1] = 1 #estado 2
        lista[2] = 0

        l_cont[1]+=1

    elif 0.9<prob<=1.0:
        lista[0] = 0
        lista[1] = 0
        lista[2] = 1 #estado 3

        l_cont[2]+=1

    return lista

def proxPartindoEstado2(lista, l_cont):
    prob = random.random()

    if prob<=0.2:
        lista[0] = 1 #estado 1
        lista[1] = 0
        lista[2] = 0

        l_cont[0]+=1

    elif 0.2<prob<=0.7:
        lista[0] = 0
        lista[1] = 1 #estado 2
        lista[2] = 0

        l_cont[1]+=1

    elif 0.7<prob<=1.0:
        lista[0] = 0
        lista[1] = 0
        lista[2] = 1 #estado 3

        l_cont[2]+=1

    return lista

def proxPartindoEstado3(lista, l_cont):
    prob = random.random()

    if prob<=0.1:
        lista[0] = 1 #estado 1
        lista[1] = 0
        lista[2] = 0

        l_cont[0]+=1

    elif 0.1<prob<=0.4:
        lista[0] = 0
        lista[1] = 1 #estado 2
        lista[2] = 0

        l_cont[1]+=1

    elif 0.4<prob<=1.0:
        lista[0] = 0
        lista[1] = 0
        lista[2] = 1 #estado 3

        l_cont[2]+=1

    return lista

def callCenterProb():
    lista = [0,1,0] # cada index indica o estado atual. O que estiver em 1 é o estado atual
    lista_contador = [0,1,0]
    for i in range(999):
        if(lista[0]): #se estiver no estado 1
            lista = proxPartindoEstado1(lista, lista_contador)
        elif(lista[1]): #se estiver no estado 2
            lista = proxPartindoEstado2(lista, lista_contador)
        elif(lista[2]): #se estiver no estado 3
            lista = proxPartindoEstado3(lista, lista_contador)

    return lista_contador

l = callCenterProb()
print("Frequência relativa com que o sistema esteve em cada estado: ")
print(f"Estado 1: {l[0]/1000} ")
print(f"Estado 2: {l[1]/1000} ")
print(f"Estado 3: {l[2]/1000} ")