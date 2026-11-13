#libreria
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL


#Crear la aplicacion
app = Flask(__name__)

app.config['TEMPLATE_AUTO_RELOAD'] = True

#Configuracion de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_albums'

app.secret_key = 'mysecretkey'

#Inicializar la base de datos
mysql = MySQL(app)

#Ruta principal: read
@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_albums')
    conAlbums = con.fetchall()
    print(conAlbums)
    return render_template('index.html', listAlbums = conAlbums)

#Ruta guardar: create
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        direccion = request.form['direccion']
        print(nombre, apellido, telefono, email, direccion)
        """CONEXION CON LA BD Y EJECUCIÓN DEL INSERT"""
        con = mysql.connection.cursor()
        con.execute('INSERT INTO tb_albums (nombre, apellido, telefono, email, direccion) VALUES(%s, %s, %s, %s, %s)', (nombre, apellido, telefono, email, direccion))
        mysql.connection.commit()
    flash('Los datos llegaron')
    return redirect(url_for('index'))

#Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
