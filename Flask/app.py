#importar los paquetes de flask
from flask import Flask, render_template, request

from werkzeug.security import generate_password_hash, check_password_hash

#instaciaion de nuestra aplicacion
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ale'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'mysecretkey'

#creacion de ruta. la ruta / es la ruta raiz
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellodo_m"]
        correo = request.form["correo"]
        password_hash = request.form["password"]
        id_rol = request.form["id_rol"]
        
        password_hasheada = generate_password_hash(password_hash) 

#iniciamos el servidor flask en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)
    #KJHG
    #JHGTYJ
    