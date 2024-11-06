from flask import Flask, render_template, request, redirect
from datetime import datetime
import uuid
#from pymongo import MongoClient
#from bson import ObjectId
from flask_cors import CORS
#from dotenv import find_dotenv, load_dotenv

app = Flask(__name__)
CORS(app)



database = {} # Definimos una base de datos temporal para hacer la prueba del CRUD montado en OpenStack


'''
Esquema de la base de datos no relacional de tareas
tarea
    _id - ObjectId()
    titulo - str
    description - str
    fechaCreacion - datetime.datetime
'''

# Ruta principal para añadir, eliminar o actualizar tareas
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        formato_fecha = '%d-%m-%Y %H:%M:%S'
        titulo = request.form["title"]
        descripcion = request.form["desc"]
        fecha_creacion = datetime.now().strftime(formato_fecha)
        _id = str(uuid.uuid4())
       
        tarea = {'_id': _id, 'titulo':titulo, 'descripcion':descripcion, 'fechaCreacion':fecha_creacion}  

        database[_id] = tarea
        #print(database)

    tareas = list(database.values())
    return render_template("index.html", all_todos=tareas)


# Ruta para actualizar tareas existentes
@app.route("/update/<string:sno>", methods=["GET", "POST"])
def update_item(sno):
    if request.method == "POST":
        user_title = request.form["title"]
        user_desc = request.form["desc"]

        titulo_nuevo = user_title if user_title else tarea['titulo']
        descr_nueva = user_desc if user_desc else tarea['descripcion']

        database[sno]['titulo'] = titulo_nuevo
        database[sno]['descripcion'] = descr_nueva
        print('hecho')
        return redirect("/")

    tarea = database[sno]
    return render_template("update.html", todo=tarea)


#Ruta para eliminar registros de la base de datos
@app.route('/delete/<sno>')
def delete_item(sno):
    datos_eliminados = database.pop(sno)
    print(datos_eliminados)
    return redirect('/')


#Ruta para búsqueda del título de una tarea en la base de datos
@app.route('/search', methods=["GET", "POST"])
def search_item():
    # Obtener la palabra clave de búsqueda del campoo query
    search_query = request.args.get('query')

    # Hacer la búsqueda en la base de datos
    tareas = [database[_id] for _id in database.keys() if database[_id]['titulo'] == search_query]

    # Mostrar el resultado
    return render_template('result.html', posts=tareas)


if __name__ == "__main__":
    #client = MongoClient('mongodb://localhost:27018/')
    #db = client['Distribuidos']
    #collection = db['tasks']
    app.run(debug=True, port=8000)
