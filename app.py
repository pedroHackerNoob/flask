#importa de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template, request

from ent.animal import Animal
from ent.brainrot import BrainRot
from ent.sorteo import Sorteo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    return render_template('animals.html', animals = Animal.get(), brains = BrainRot.get() )

@app.route('/sorteo', methods=['GET', 'POST'])
def sorteo():
    num1 = request.form.get('num1')
    if request.method == 'POST':
        print(num1)
        return render_template('sorteo.html', body = num1)
    else:
        return render_template('sorteo.html')


if __name__ == '__main__':
    app.run()