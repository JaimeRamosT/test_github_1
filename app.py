from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hola Mundo!</h1>"


# Ejemplo de ruta: /suma?num1=5&num2=3
@app.route("/suma")
def suma():
    # Obtener los parámetros desde la URL
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    # Calcular la suma
    result = num1 + num2

    # Retornar el resultado como una cadena de texto
    return f"La suma de {num1} y {num2} es: {result}"


if __name__ == "__main__":
    app.run()
