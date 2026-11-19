from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# CONEXIÓN A MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_contactos'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)


# RUTA PRINCIPAL: READ (Listar contactos)
@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_contactos')
    datos = con.fetchall()
    con.close()
    return render_template('index.html', listContactos=datos)


# RUTA CREATE (Guardar contacto)
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        apellido = request.form['txtApellido']
        telefono = request.form['txtTelefono']
        email = request.form['txtEmail']
        direccion = request.form['txtDireccion']

        con = mysql.connection.cursor()
        con.execute(
            'INSERT INTO tb_contactos (nombre, apellido, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)',
            (nombre, apellido, telefono, email, direccion)
        )
        mysql.connection.commit()
        con.close()

        flash('¡El contacto fue agregado correctamente!')
        return redirect(url_for('index'))


# RUTA PARA MOSTRAR FORMULARIO DE EDICIÓN
@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_contactos WHERE id = %s', (id,))
    contacto = con.fetchone()
    con.close()
    return render_template('editarContacto.html', contacto=contacto)


# RUTA UPDATE (Actualizar contacto)
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        apellido = request.form['txtApellido']
        telefono = request.form['txtTelefono']
        email = request.form['txtEmail']
        direccion = request.form['txtDireccion']

        con = mysql.connection.cursor()
        con.execute(
            'UPDATE tb_contactos SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s WHERE id=%s',
            (nombre, apellido, telefono, email, direccion, id)
        )
        mysql.connection.commit()
        con.close()

        flash(f'Se actualizó el contacto: {nombre} {apellido}')
        return redirect(url_for('index'))


# RUTA PARA MOSTRAR VISTA DE CONFIRMACIÓN DE ELIMINACIÓN
@app.route('/confirmar_eliminar/<int:id>')
def confirmar_eliminar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_contactos WHERE id = %s', (id,))
    contacto = con.fetchone()
    con.close()
    return render_template('eliminarContacto.html', contacto=contacto)


# RUTA DELETE (Eliminar contacto)
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        nombre = request.form.get('txtNombre', '')
        con = mysql.connection.cursor()
        con.execute('DELETE FROM tb_contactos WHERE id = %s', (id,))
        mysql.connection.commit()
        con.close()

        flash(f'Se eliminó el contacto: {nombre}')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)