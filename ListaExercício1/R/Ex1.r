lcg <- function(a,c,M,xo,qtd,low=0, high=0){
    lista <- c()
    for (i in 1:qtd){
        xo = (a*xo+c)%%M
        uk = xo/M

        if (low==0 && high==0){
            lista <- c(lista, uk) 
        }
        else{
            resultado = low+(high-low)*uk
            lista <- c(lista, resultado) 
        }
    }
    return(list(valores = lista, ultimo_x = xo))
}

a = 39373
c = 0
M = 2^31 - 1
xo= 3

l_forca = lcg(a,c,M,xo,10,10,20)
lista = l_forca$valores
xo = l_forca$ultimo_x 

l_agil = lcg(a,c,M,xo,10,5,15)
lista = l_agil$valores
xo = l_agil$ultimo_x 

l_smart = lcg(a,c,M,xo,10,8,18)
lista = l_smart$valores
xo = l_smart$ultimo_x 
for (j in 1:10){
    cat("Personagem", j, 
    "| Inteligencia:", l_smart$valores[j],
    "| Forca:", l_forca$valores[j],
    "| Agilidade:", l_agil$valores[j],
    "\n")
}
