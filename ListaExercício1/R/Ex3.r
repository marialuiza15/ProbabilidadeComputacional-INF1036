set.seed(123)

quem_vence <- function(lt1, lt2){
    if (lt1=='A'){
        if (lt2=='B'){
            vencedor <- sample(c('A','B'),size=1,prob=c(0.6,0.4))
        }
        if (lt2=='C'){
            vencedor <- sample(c('C','A'),size=1,prob=c(0.55,0.45))
        }
    }
    if (lt1=='B'){
        if (lt2=='A'){
            vencedor <- sample(c('A','B'),size=1,prob=c(0.6,0.4))
        }
        if (lt2=='C'){
            vencedor <- sample(c('B','C'),size=1,prob=c(0.65,0.35))
        }
    }
    if (lt1=='C'){
        if (lt2=='A'){
            vencedor <- sample(c('C','A'),size=1,prob=c(0.55,0.45))
        }
        if (lt2=='B'){
            vencedor <- sample(c('B','C'),size=1,prob=c(0.65,0.35))
        }
    }
    return(vencedor)
}

simular <- function(){
    prob = runif(1)
    if (prob<=0.4){
        vencedor <- quem_vence('B','C')
        descansado <-'A'
    }
    if (0.4<prob & prob<=0.7){
        vencedor <- quem_vence('A','C')
        descansado <-'B'
    }
    if (0.7<prob & prob<=1){
        vencedor <- quem_vence('A','B')
        descansado <-'C'
    }
    vencedor_segundo <- quem_vence(vencedor,descansado)
    return(vencedor_segundo)
}

cont_a = 0
cont_b = 0
cont_c = 0

for (i in 1:1000){
    vencedor <- simular()
    if (vencedor=='A'){
        cont_a = cont_a+1
    }
    if (vencedor=='B'){
        cont_b = cont_b+1
    }
    if (vencedor=='C'){
        cont_c = cont_c+1
    }
}

cat("probabilidade do lutador A vencer a etapa: ", cont_a/1000)
cat("\nprobabilidade do lutador B vencer a etapa: ", cont_b/1000)
cat("\nprobabilidade do lutador C vencer a etapa: ", cont_c/1000)