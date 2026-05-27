set.seed(123)

cont_falhas_totais <- 0
substituicoes <- 0
custo_total <- 0

for (i in 1:1000){
    vida_util <- 1.0
    for (h in 1:720){
        prob <- runif(1)
        if (prob <= 0.002){
            cont_falhas_totais <- cont_falhas_totais + 1
            substituicoes  <- substituicoes  + 1
            custo_total <- custo_total + 2000
            vida_util <- 1.0
        }
        else{
            red_vida <- sample(c(0.01,0.03,0.07),size=1,prob=c(0.70,0.20,0.10))
            vida_util <- vida_util-red_vida
            if (vida_util<=0){
                substituicoes  <- substituicoes  + 1
                if (red_vida == 0.01){
                    custo = 400
                }
                if (red_vida == 0.03){
                    custo = 500
                }
                if (red_vida == 0.07){
                    custo = 700
                }
                custo_total <- custo_total + custo 
                vida_util <- 1.0
            }
        }
    }
}

cat("Media de substituição por simulação: ", substituicoes /1000)
cat("O custo médio total por simulação: ", custo_total/1000)
cat("O número médio de falhas totais aleatórias: ", cont_falhas_totais/1000)
cat("\n")