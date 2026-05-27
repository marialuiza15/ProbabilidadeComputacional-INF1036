set.seed(123)

presente <- 0
fila_prioridade <- 0
compensacao <- 0
qtd_vol <- 0
qtd_forc <- 0
qtd_overbooking <-0
presente <- 0


for(i in 1:100){
    for(i in 1:20){
        presente <- 0
        if(fila_prioridade>0){
            presente <- fila_prioridade
            fila_prioridade <- 0 
        }
        eh_over = FALSE
        for(i in 1:190){
            prob_individual <- runif(1, 0.90,0.95)
            prob <- rbinom(1,1,prob_individual) #sorteia 0 ou 1, ou seja, TRUE ou FALSE com probabilidade prob
            
            if (prob){
                if (presente>180){
                    if(eh_over==FALSE){
                        qtd_overbooking <- qtd_overbooking + 1
                        eh_over <- TRUE
                    }
                    fila_prioridade <- fila_prioridade+1
                    prob_escedente <- runif(1)
                    if(prob_escedente<=0.25){
                        compensacao <- compensacao + 1000
                        qtd_vol <- qtd_vol + 1
                    }
                    else{
                        compensacao <- compensacao + 2500
                        qtd_forc <- qtd_forc + 1
                    }
                }
                else{
                    presente <- presente +1
                }
            }
        }
    }
}

cat("taxa média de overbooking", qtd_overbooking/(20*100),"\n")
cat("custo total das compensações", compensacao, "\n")
cat("custo médio diário das compensações", compensacao/100, "\n")
cat("quantos passageiros foram realocados voluntariamente", qtd_vol, "\n")
cat("quantos passageiros foram realocados forçados", qtd_forc, "\n")