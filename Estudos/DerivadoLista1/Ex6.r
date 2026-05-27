set.seed(123)

estimar_prob_condicional <- function(n=100000) {
  
  count_AeB <- 0
  count_B <- 0
  
  for(i in 1:n) {
    res <- experimento()
    
    if(res$B) {
      count_B <- count_B + 1
      
      if(res$A) {
        count_AeB <- count_AeB + 1
      }
    }
  }
  
  if(count_B == 0) {
    return(0)
  }
  
  return(count_AeB / count_B)
}

cat("P(A|B) ≈", estimar_prob_condicional(), "\n")