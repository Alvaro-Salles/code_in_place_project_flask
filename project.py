from flask import Flask, render_template, request
import random

app = Flask(__name__)

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

@app.route('/', methods=['GET', 'POST'])
def index():
    planet = None
    stars = generate_stars()
    message = "Bem-vindo ao Planetarium! Escolha um planeta para visualizar."
    if request.method == 'POST':
        selected_planet = request.form['planet'].lower().strip()
        if selected_planet in planet_dict:
            planet = selected_planet
            message = f"Você está visualizando: {selected_planet.capitalize()}"
        else:
            message = "Por favor, selecione um planeta válido."
    return render_template('index.html', planet=planet, stars=stars, message=message, planet_data=planet_dict.get(planet))

def generate_stars():
    stars = []
    for _ in range(int((CANVAS_HEIGHT + CANVAS_WIDTH) / 8)):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        size = random.randint(1, 2)
        stars.append({'x': x, 'y': y, 'size': size})
    return stars

planet_dict = {
    'mercury': {'color': 'darkgoldenrod', 'size': 20},
    'venus': {'color': 'goldenrod', 'size': 50},
    'earth': {'color': 'royalblue', 'size': 50},
    'mars': {'color': 'red', 'size': 20},
    'jupiter': {'color': 'burlywood', 'size': 300},
    'saturn': {'color': 'tan', 'size': 300},
    'uranus': {'color': 'cyan', 'size': 230},
    'neptune': {'color': 'dodgerblue', 'size': 230},
    'sun': {'color': 'yellow', 'size': 1000},
    'pluto': {'color': None, 'size': None}
}

if __name__ == '__main__':
    app.run(debug=True)
