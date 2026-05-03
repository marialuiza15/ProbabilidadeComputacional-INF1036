calcula_paralelo <- function(...){
    probs <- c(...) #ele combina (c) todos os pametros que a função recebe e comoloca no vetor probs
    return(1-prod(1-probs)) #faz o produto de (1-probs[i]), ou sjea, para todos os parametros.
}

calcula_total <- function(){
    par_esq <- calcula_paralelo(0.88,0.89)
    par_dir <- calcula_paralelo(0.91,0.89,0.88)
    serial <-0.97

    return(par_esq*par_dir*serial)
}

cat("Probabilidade do circuito funcionar: ", calcula_total(), "\n")
