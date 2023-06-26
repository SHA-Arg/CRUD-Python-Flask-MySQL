from flask import Flask, render_template , request, url_for, redirect
import os
import database as db

# esta linea brinda acceso a la carpeta del projecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# esta linea une las carpetas src y templates a la carpeta del projecto
template_dir = os.path.join(template_dir, 'src','templates')


app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicacion
@app.route('/')
def home():
    # Creando contulta a la base de datos
    cursor = db.database.cursor()
    # Tipo de consulta
    cursor.execute('SELECT * FROM users')
    # Obteniendo los datos de la consulta en una tupla para luego convertir a diccionario
    myresult = cursor.fetchall()
    # Convertiendo tupla a diccionario
    insertObject = []
    # Establecer los datos con las claves de cada campo
    columnNames = [column[0] for column in cursor.description]
    # bucle para ir agregando los datos al diccionario
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    # Para maquetar los datos especificar como enviarlos a la vista
    return render_template('index.html', data = insertObject)


# Ruta para guardar usuarios a la base de datos
@app.route('/user', methods=['POST'])
def saveUser():
    username = request.form['username']
    name  = request.form['name']
    password = request.form['password']

    # Condicion para que si tenemos todos los datos se realice la consulta
    if username and name and password:
        cursor = db.database.cursor()
        # Consulta
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        # Tupla para pasarle los datos
        data = (username, name, password)
        # Ejecutando la consulta
        cursor.execute(sql, data)
        # Commit a la base de datos
        db.database.commit()
    # Para actualizar la vista
    return redirect(url_for('home'))

# Esta linea lanza la aplicacion
if __name__ == '__main__':
    # Modo desarrollo
    app.run(debug=True, port=4000)
