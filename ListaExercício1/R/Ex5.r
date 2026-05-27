set.seed(123)
GRID_MIN <-1
GRID_MAX <-11

gera_posicoes_unicas <- function(n, excluir){
    pos <- list()
    
    while(length(pos)<n){ #em r len vira length
        p <- c(
            sample(GRID_MIN:GRID_MAX,size=1),
            sample(GRID_MIN:GRID_MAX,size=1)
        )
        ja_existe <- any(sapply(excluir, function(x) all(x==p)))
        if(!ja_existe){
            pos[[length(pos)+1]] <- p
        }
    }
    return(pos)
}

mover <- function(pos){
    x <- pos[1]
    y <- pos[2]

    l_movimentos <- list(c(1,0),c(-1,0),c(0,1),c(0,-1))
    mov <- l_movimentos[[sample(length(l_movimentos), 1)]]
    dx <- mov[1]
    dy <- mov[2]
    return(c(
        max(GRID_MIN, min(GRID_MAX, x+dx)),
        max(GRID_MIN, min(GRID_MAX, y+dy))
    ))
}

etapa <- function(estado){
    pos_pac = mover(estado$pos_pac)
    pos_ini = lapply(estado$pos_ini, mover)
    pos_obj = estado$pos_obj

    ja_existe <- any(sapply(pos_ini, function(x) all(x==pos_pac)))
    if(ja_existe){
        return(list(status="derrota", estado=estado))
    }

    ja_existe <- any(sapply(pos_obj, function(x) all(x==pos_pac)))
    if(ja_existe){
        pos_obj[sapply(pos_obj, function(p) all(p==pos_pac))] <- NULL #pos_obj.remove(pos_pac)
        estado$pos_obj = pos_obj
        if(length(pos_obj)==0){
            return(list(status="vitoria", estado=estado))
        }
    }

    estado$pos_pac = pos_pac
    estado$pos_ini = pos_ini
    return(list(status="continua", estado=estado))
}

cont <- 0
simula <-function(){
    estado <- list(
        pos_pac = c(1,1),
        pos_ini = list(c(1,1),c(11,11),c(1,11)),
        pos_obj = gera_posicoes_unicas(4, list(c(1,1))),
        vidas = 1
    )

    for(i in 1:1000){
        resultado  <- etapa(estado)
        estado <- resultado$estado
        status <- resultado$status
        if(status!="continua"){
            if(status=="vitoria"){
                return(1)
            }
            else{
                return(0)
            }
        }
    }
    return(0)
}

for(i in 1:1000){
    cont <- cont + simula()  # ✅ opção 2: simula() retorna 0 ou 1
}

cat(cont/1000)