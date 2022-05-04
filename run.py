#Importar
from flask import Flask

#Crear app medante instancia
app = Flask(__name__)

#Crear rutas
@app.route('/', methods=['GET'])  #Indicamos metodo GET
def holamundo():
    return 'Hola Mundo!'


@app.route('/sobremi', methods=['GET'])
def sobremi():
    return 'Aquí se mostrarán mis proyectos'








#Ejecutar nuestra app con run.py

if __name__ == '__main__':

    app.run(debug=True)