from flask import Flask, render_template, request, redirect, url_for
from generacion import build_dungeon_map
from movimiento import tecla_w, tecla_a, tecla_s, tecla_d

app = Flask(__name__)

# Estado global del juego
width, height = 10, 10
jugador = [int(width/2), int(height/2)]
dungeon_map = build_dungeon_map(width, height, jugador)


# Función para mover al jugador según dirección
def mover(direccion):
    global dungeon_map, jugador
    if direccion == "w":
        dungeon_map, jugador = tecla_w(dungeon_map, jugador)
    elif direccion == "a":
        dungeon_map, jugador = tecla_a(dungeon_map, jugador)
    elif direccion == "s":
        dungeon_map, jugador = tecla_s(dungeon_map, jugador)
    elif direccion == "d":
        dungeon_map, jugador = tecla_d(dungeon_map, jugador)

# Ruta principal
@app.route("/")
def index():
    return render_template("mapa.html", mapa=dungeon_map)

# Ruta para mover al jugador
@app.route("/mover/<dir>")
def mover_ruta(dir):
    mover(dir)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
