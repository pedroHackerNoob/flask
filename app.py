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

    if request.method == 'POST':
        data = request.get_json()
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))

        print(num1," numeros ",num2)
        sorteo = Sorteo(num1, num2)
        resultado = sorteo.iniciarSorteo()

        return render_template('sorteo.html', resultado = resultado)
    else:
        return render_template('sorteo.html')


if __name__ == '__main__':
    app.run()