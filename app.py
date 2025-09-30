#importa de un paquete llamado flask, una clase llamada Flask
from flask import Flask, render_template

#Estamos creando un objeto a partir del constructor de la clase 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animals')
def animals():
    return render_template('animals.html')

if __name__ == '__main__':
    app.run()