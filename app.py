#importa de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template, request

from ent.animal import Animal
from ent.brainrot import BrainRot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    return render_template('animals.html', animals = Animal.get(), brains = BrainRot.get() )

@app.route('/brainroot')
def animalname():
    return render_template('ShowBrainRoot.html')

if __name__ == '__main__':
    app.run()