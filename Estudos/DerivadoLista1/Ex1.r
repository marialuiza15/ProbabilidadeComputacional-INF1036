#ERRADO

set.seed(123)
LCG <- function(a,c,M,xo,qtd,low=0,high=0){
    lista <- c() #cria lista vazia lista<- []
    for(i in 1:qtd){
        xo <- (a*xo+c)%%M
        uk <- xo/M

        if(low==0 && high==0){
            lista <- c(lista, uk) #lista.append(uk)
        }
        else{
            resultado <- low+(high-low)*uk
            lista <- c(lista, resultado) #lista.append(resultado)
        }
            
    }
    return(c(lista,xo))
}

exibe <- function(l){
    cat("Cartas geradas com LCG: ")
    for( i in 1:15){
        cat(sprintf("%d°: %d", i+1, l[i]))
    }
}

gera_atributos_LCG <- function(){
    a = 16807
    c = 0
    M = 2**31-1
    xo = 7

    l_cartas <- c() #l_cartas = []
    for(i in 1:15){
        l_ataque, xo = LCG(a,c,M,xo,1,low=15,high=30)
        ataque = l_ataque[0]

        l_defesa, xo = LCG(a,c,M,xo,1,low=5,high=20)
        defesa = l_defesa[0]

        l_magia, xo = LCG(a,c,M,xo,1,low=0,high=10)
        magia = l_magia[0]

        l_cartas.append <- c(lista, [ataque, defesa, magia])
    }

    exibe(l_cartas)

    ataque  = [a[0] for(c in names(l_cartas))]
    defesa  = [a[0] for(c in names(l_cartas))]
    magia  = [a[0] for(c in names(l_cartas))]

    return(c(ataque,defesa,magia))
}

gera_atributos_random <- function(){
    l_cartas <- c() #l_cartas = []
    for(i in 1:15){
        ataque = runif(15,30)
        defesa = runif(5,20)
        magia = runif(0,10)

        l_cartas.append <- c(lista, [ataque, defesa, magia])
    }

    exibe(l_cartas)

    ataque  = [a[0] for(c in names(l_cartas))]
    defesa  = [a[0] for(c in names(l_cartas))]
    magia  = [a[0] for(c in names(l_cartas))]

    return(c(ataque,defesa,magia))
}

estatistica <- function(nome, dados){
    cat(sprintf("%s", nome))
    cat(sprintf("Média:", np.mean(dados)))
    cat(sprintf("Desvio padrão:", np.std(dados)))
    cat(sprintf("Min:", np.min(dados)))
    cat(sprintf("Max:", np.max(dados)))
}

hist <- function(tit, dado1, dado2){
    plt.hist(dado1, alpha=0.5, label="LCG")
    plt.hist(dado2, alpha=0.5, label="Python")
    plt.title(tit)
    plt.legend()
    plt.show()
}

ataque_lcg, defesa_lcg, magia_lcg = gera_atributos_LCG()
cat("\n")
ataque_py, defesa_py, magia_py = gera_atributos_Random()

estatistica("Ataque LCG", ataque_lcg)
estatistica("Ataque Python", ataque_py)

estatistica("Defesa LCG", defesa_lcg)
estatistica("Defesa Python", defesa_py)

estatistica("Magia LCG", magia_lcg)
estatistica("Magia Python", magia_py)

hist("Ataque", ataque_lcg,ataque_py)
hist("Defesa", defesa_lcg,defesa_py)
hist("Magia", magia_lcg,magia_py)