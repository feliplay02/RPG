def build_dungeon_map(width, height, jugador):
    map = [[" " for _ in range(width)] for _ in range(height)]
    for y in range(0, height):
        for x in range(0,width):
            if y == 0 or y == (height-1) or x == 0 or x == (width-1):
                map [y][x] = "#"
            elif y == jugador[1] and x == jugador[0]:
                map [y][x] = "P"
            else:
                map [y][x] = "."
    return map