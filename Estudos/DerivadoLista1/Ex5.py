import random
random.seed(123)

GRID_MIN, GRID_MAX = 1,9

def gerar_posicoes_unicas(n, excluir=set()):
    pos = set()
    while len(pos)<n:
        p = (random.randint(GRID_MIN, GRID_MAX),
             random.randint(GRID_MIN, GRID_MAX))
        if p not in excluir:
            pos.add(p)
    return pos


def mover(pos):
    x,y = pos
    dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
    return (max(GRID_MIN,min(GRID_MAX,x+dx)),
            max(GRID_MIN,min(GRID_MAX,y+dy)))

def etapa(estado):
    pos_protagonista = mover(estado["pos_protagonista"])
    pos_inimigos = [mover(d) for d in estado["pos_inimigos"]]
    pos_objetivos = estado["pos_objetivos"]

    if pos_protagonista in pos_objetivos:
        pos_objetivos.remove(pos_protagonista)
        estado["pos_objetivos"] = pos_objetivos
        if len(pos_objetivos) == 0:
            return "vitoria"

    if pos_protagonista in pos_inimigos:
        return "derrota"

    estado["pos_protagonista"] = pos_protagonista
    estado["pos_inimigos"] = pos_inimigos

    return "continua"

def simulacao():
    estado = {
        "pos_protagonista": (5,5),
        "pos_inimigos": [(1,1),(9,9)],
        "pos_objetivos": gerar_posicoes_unicas(5, {(5,5)}),
        "vidas": 1
    }

    for _ in range(1000):
        status = etapa(estado)
        if status != "continua":
            return 1 if status == "vitoria" else 0
    return 0

def monte_carlo(n=1000):
    return sum(simulacao() for _ in range(n)) / n

print("Probabilidade de vitória:", monte_carlo())