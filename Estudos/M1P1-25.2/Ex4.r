set.seed(123)

custo <- function(area){
    return(volume(area)*250)
}

volume <- function(area){
    return(area*6)
}

gera_coord <- function(){
    x = runif(1,0,1)
    y = runif(1,0,1)

    return(c(x,y))
}

estima_area <- function(){
    coord <- gera_coord()
    x <- coord[1]
    y <- coord[2]
    if(x>=0.5 && y >= 0.5 && (x**2 + y**2 >= 1)) {
        return(1)
    }
    return(0)
}

dentro = 0
for(i in 1:10000){
    dentro <- dentro + estima_area()
}

area = dentro / 10000
cat("Area estimada:", area)
cat("\nCusto estimado: ", custo(area))