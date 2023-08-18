from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')
def hello():
    return '<h1>Hello, There!</h1>'



@app.route('/multiplicar')
def multiplicar():
    # Obtener los parámetros desde la URL
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    # Calcular la multiplicacion
    result = num1 * num2

    # Retornar el resultado como una cadena de texto
    return f"La multiplicacion de {num1} y {num2} es: {result}"
