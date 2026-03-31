'''
cara = 0 
coroa = 1

n=qtd lancamentos da moeda

se n=5 entao podemos gerar numeros de 0 a (2^5 - 1)

o numero de lancamentos diz o numero de digitos, para n=5 teremos 5 digitos binarios,q ue quando convertemos para demical, dará o psedoaletorio


'''
a = 39373
c = 0
M = 2**31 - 1
x0=3

def pseudoaleatorioLCG(a, c, M, x0, min, max, qtd):
    lista = []
    for i in range(qtd):
        aux = (a*x0+c) # x+1 = (a*x0+c)*mod M
        xProx = aux%M
        x0=xProx # x0 = x+1
        lista.append(xProx)
     
    listaNumerosNormalizados=[]

    for i in range(qtd):
        resultado = min+(max-min)*lista[i]/M
        listaNumerosNormalizados.append(resultado)
    
    return listaNumerosNormalizados

#a)
def lancaMoedas():
    
        chance = pseudoaleatorioLCG(a, c, M, x0, 0, 1, 10000)
        dict_moedas = {}
        for prob in chance:
            if prob<0.5:
                dict_moedas["cara"]= dict_moedas.setdefault("cara", 0)+1
            else:
                dict_moedas["coroa"]= dict_moedas.setdefault("coroa", 0)+1

        print(f"{dict_moedas['cara']} moedas deram CARA\n{dict_moedas['coroa']} moedas deram COROA")
        return dict_moedas

def lancaDados():
    import numpy as np
    chance = np.random.sample(10000)
    dict_dados = {}

    dict_dados["1"]= [dict_dados["1"]= dict_dados.setdefault("1", 0)+1  if prob>0 and prob<=0.125  else pass  for prob in chance]
    print(dict_dados["1"])
    
    for prob in chance:
        if prob>0 and prob<=0.125:
            dict_dados["1"]= dict_dados.setdefault("1", 0)+1
        if prob>0.125 and prob<=0.25:
            dict_dados["2"]= dict_dados.setdefault("2", 0)+1
        if prob>0.25 and prob<=0.375:
            dict_dados["3"]= dict_dados.setdefault("3", 0)+1
        if prob>0.375 and prob<=0.5:
            dict_dados["4"]= dict_dados.setdefault("4", 0)+1
        if prob>0.5 and prob<=0.625:
            dict_dados["5"]= dict_dados.setdefault("5", 0)+1
        if prob>0.625 and prob<=0.750:
            dict_dados["6"]= dict_dados.setdefault("6", 0)+1    
        if prob>0.750 and prob<=0.875:
            dict_dados["7"]= dict_dados.setdefault("7", 0)+1
        if prob>0.875 and prob<=1:
            dict_dados["8"]= dict_dados.setdefault("8", 0)+1

    print(f"{dict_dados['1']} -> LADO 1\n{dict_dados['2']} -> LADO 2\n{dict_dados['3']} -> LADO 3\n{dict_dados['4']} -> LADO 4\n{dict_dados['5']} -> LADO 5\n{dict_dados['6']} -> LADO 6\n{dict_dados['7']} -> LADO 7\n{dict_dados['8']} -> LADO 8\n")
    return dict_dados




#b)
def lancaMoedaDado():
    dict_moedas = lancaMoedas()
    dict_dados = lancaDados()


lancaMoedaDado()

