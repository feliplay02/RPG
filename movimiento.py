

def tecla_w(mapa, jugador):
    if mapa[jugador[0] - 1][jugador[1]] != "#":
        mapa[jugador[0]][jugador[1]] = "."
        jugador[0] -= 1
        mapa[jugador[0]][jugador[1]] = "P"
    return mapa, jugador

def tecla_a(mapa, jugador):
    if mapa[jugador[0]][jugador[1] - 1] != "#":
        mapa[jugador[0]][jugador[1]] = "."
        jugador[1] -= 1
        mapa[jugador[0]][jugador[1]] = "P"
    return mapa, jugador

def tecla_s(mapa, jugador):
    if mapa[jugador[0] + 1][jugador[1]] != "#":
        mapa[jugador[0]][jugador[1]] = "."
        jugador[0] += 1
        mapa[jugador[0]][jugador[1]] = "P"
    return mapa, jugador

def tecla_d(mapa, jugador):
    if mapa[jugador[0]][jugador[1] + 1] != "#":
        mapa[jugador[0]][jugador[1]] = "."
        jugador[1] += 1
        mapa[jugador[0]][jugador[1]] = "P"
    return mapa, jugador

