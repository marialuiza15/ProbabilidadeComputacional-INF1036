def calcula_paralelo(p1,p2,p3=0):
    if(p3==0):
        return 1-((1-p1)*(1-p2))
    else:
        return 1-((1-p1)*(1-p2)*(1-p3))

def calcula_total():
    par_esq = calcula_paralelo(0.88,0.89)
    par_dir = calcula_paralelo(0.91,0.89,0.88)
    serial = 0.97

    return par_esq*par_dir*serial

print("Probabilidade do circuito funcionar: ", calcula_total())
    