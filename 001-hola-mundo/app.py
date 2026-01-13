from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

'''
    podemos retornar HTML directamente desde una ruta de Flask
'''
def responsehtml():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo</title>
    </head>
    <body>
        <h1>¡Hola, Mundo!</h1>
        <p>Esta es una página HTML simple servida con Flask.</p>
    </body>
    </html>
    '''

'''
    ruta que retorna HTML directamente con un saludo personalizado
'''
@app.route('/hola/<name>')
def bienvenido(name):
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bienvenido</title>
    </head>
    <body>
        <h1>¡Bienvenido, {}!</h1>
        <p>Nos alegra tenerte aquí.</p>
    </body>
    </html>
    '''.format(name)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

