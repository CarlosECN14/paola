from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from database import Database
from database import engine
from database import db_session
from flask import url_for
import models


app = Flask(__name__)
    
Database.metadata.create_all(engine)

@app.get('/')
def home():
    producto = db_session.query(models.muebles).all()
    return render_template("home.html", producto=producto)

@app.get('/agregar')
def agregar():
    return render_template("agregar.html")

@app.post('/agregar_producto')
def create():
    nombre = request.form['nombre']
    dimensiones = request.form['dimensiones']
    material = request.form['material']
    precio = request.form['precio']

    nuevo_mueble = models.muebles(
        nombre = nombre,
        dimensiones = dimensiones,
        material = material,
        precio = precio
    )

    db_session.add(nuevo_mueble)
    db_session.commit()
    return redirect(url_for('home') + "crud_paola")

@app.get('/actualizar/<id>')
def editar(id):
    producto= db_session.query(models.muebles).get(id)
    return render_template('editar.html', producto=producto)

@app.post('/<id>/actualizar')
def editar_producto(id):
    producto= db_session.query(models.muebles).get(id)

    nombre = request.form['nombre']
    dimensiones = request.form['dimensiones']
    material = request.form['material']
    precio = request.form['precio']

    if nombre and nombre != '':
        producto.nombre = nombre
    
    if dimensiones and dimensiones != '':
        producto.dimensiones = dimensiones

    if material and material != '':
        producto.material = material 

    if precio and precio != '':
        producto.precio = precio

    db_session.add(producto)
    db_session.commit()
    return redirect(url_for('home') + "crud_paola") 



@app.get('/eliminar/producto/<id>/')
def eliminar_producto(id):
    producto = db_session.query(models.muebles).get(id)
    db_session.delete(producto)
    db_session.commit()
    return redirect(url_for('home') + "crud_paola")   

    
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 7777, debug=True)
    
    