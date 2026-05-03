set.seed(123)

calcula_area <- function(x1,y1,x2,y2,x3,y3){
    return(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
}

verifica_qualidade <- function(prop){
    if (prop<0.05){
        return("Ruim")
    } 
    if (0.05<=prop && prop<0.1){
        return("Média")
    } 
    if (0.1<=prop && prop<0.2){
        return("Boa")
    } 
    if (prop>=0.2){
        return("Excelente")
    } 
}

estima_cobertura <- function(){
    x1 = runif(1, 0, 100) # runif(n, min, max)
    y1 = runif(1, 0, 100)
    x2 = runif(1, 0, 100)
    y2 = runif(1, 0, 100)
    x3 = runif(1, 0, 100)
    y3 = runif(1, 0, 100)
    proporcao = calcula_area(x1,y1,x2,y2,x3,y3)/(100*100)
    
    return(verifica_qualidade(proporcao))
}


d_qual_qtd <- c(Ruim=0, Média=0, Boa=0, Excelente=0) #nao existe dicionario, existe combinação, que gera um tipo de vetor
for (i in 1:1000){
    qual = estima_cobertura()
    d_qual_qtd[qual] <- d_qual_qtd[qual] +1
}
    
cat("Probabilidades:")
for (k in names(d_qual_qtd)){
    cat(sprintf("%s :%.3f\n",k,d_qual_qtd[k]/1000))
}
    