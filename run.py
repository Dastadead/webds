#Importar
from flask import Flask , render_template

#Crear app medante instancia
app = Flask(__name__)

#Crear rutas
@app.route('/', methods=['GET'])  #Indicamos metodo GET
def holamundo():
    return render_template('index.html')


@app.route('/sobremi', methods=['GET'])
def sobremi():
    return render_template('sobremi.html')


#CONTACTO
@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template('/contacto.html')





#Ejecutar nuestra app con run.py

if __name__ == '__main__':

    app.run(debug=True)