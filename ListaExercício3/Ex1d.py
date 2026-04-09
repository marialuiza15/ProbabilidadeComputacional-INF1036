import random
random.seed(123)

def LCG(a,c,M,x0,qtd,low=0,high=0):
    lista=[]
    for _ in range(qtd):
        x0 = (a*x0+c)%M
        uk = x0/M

        if low==0 and high==0:
            lista.append(uk)
        else:
            resultado = low+(high-low)*uk
            lista.append(resultado)
    return lista, x0

def LM(x0, lancamentos):
    bits = []
    for _ in range(lancamentos):
        uk, x0 = LCG(39373,0,2**31 - 1,x0,1,low=0,high=1)

        if uk[0]<0.5:
            bits.append(0) #cara
        else:
            bits.append(1) #coroa

    tam = lancamentos - 1
    numeroFinal = 0

    for bit in bits:
        numeroFinal += bit*(2**tam)
        tam-=1

    return numeroFinal, x0

def lancaMoeda():
    return random.choices(['cara','coroa'], weights=(0.45,0.55))[0]

def lancaDado(x0):
    numero, x0 = LM(x0,10)
    indice = numero%8
    faces = [1,2,3,4,5,6,7,8]
    return faces[indice], x0
    
def lancaMoedaDado():
    x0=3
    d_comb={'cara_face1': 0, 'cara_face4':0, 'coroa_face7': 0}
    
    for _ in range(10000):
        moeda = lancaMoeda()
        dado, x0 = lancaDado(x0)

        if moeda=='cara' and dado==1:
            d_comb['cara_face1']+=1
        elif moeda=='cara' and dado==4:
            d_comb['cara_face4']+=1
        if moeda=='coroa' and dado==7:
            d_comb['coroa_face7']+=1

    probabilidade = (d_comb.get('cara_face1')+d_comb.get('cara_face4')+d_comb.get('coroa_face7'))/10000

    print("Probabilidade de se obter pelo menos um dos resultados: simultaneamente cara e face 1; simultaneamente cara e face 4;simultaneamente coroa e face 7: ", probabilidade)

lancaMoedaDado()