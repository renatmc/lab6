from flask import Flask, flash, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'alumnos_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        email = request.form['email']
        contra = request.form['contra'].encode('utf-8')
        hash_password = bcrypt.hashpw(contra, bcrypt.gensalt())
        tipo = request.form['tipo']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuario (codigo,nombre,email,contra,tipo) VALUES (%s,%s,%s,%s,%s)",(codigo,nombre,email,hash_password,tipo,))
        mysql.connection.commit()
        session['codigo'] = codigo
        session['nombre'] = nombre
        session['email'] = email
        return redirect(url_for("home"))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        contra = request.form['contra'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM usuario WHERE email=%s",(email,))
        usuario = cur.fetchone()
        cur.close()

        if len(usuario) > 0:
            if bcrypt.hashpw(contra, usuario['contra'].encode('utf-8')) == usuario['contra'].encode('utf-8'):
                session['codigo'] = usuario['codigo']
                session['nombre'] = usuario['nombre']
                session['email'] = usuario['email']
                return render_template("index.html")
        else:
            return "Contraseña erronea"
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")
    
if __name__ == '__main__':
    app.secret_key = "lol"
    app.run(port=3000,debug=True)