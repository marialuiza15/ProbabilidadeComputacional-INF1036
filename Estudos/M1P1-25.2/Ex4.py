import random

random.seed(123)

def custo(area_base_cinza):
    return volume(area_base_cinza)*250

def volume(area):
    return area*6

def gera_coord():
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    return(x,y)

def estima_area():
    x,y = gera_coord()
    if x >= 0.5 and y >= 0.5 and (x**2 + y**2 >= 1):
        return 1
    return 0

dentro= 0
for _ in range(10000):
    dentro += estima_area()

area = dentro / 10000
print("Área estimada:", area)
print("Custo estimado:", custo(area))