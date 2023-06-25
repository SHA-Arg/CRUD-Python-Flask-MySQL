from flask import Flask, render_template
import os

# esta linea brinda acceso a la carpeta del projecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# esta linea une las carpetas src y templates a la carpeta del projecto
template_dir = os.path.join(template_dir, 'src','templates')


app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicacion
@app.route('/')
def home():

    return render_template('index.html')

# esta linea lanza la aplicacion
if __name__ == '__main__':
    #modo desarrollo
    app.run(debug=True, port=4000)
