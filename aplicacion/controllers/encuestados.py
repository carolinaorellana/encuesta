from aplicacion import app
from flask import Flask, render_template, render_template, request, redirect, session
from aplicacion.models.encuestado import Encuestado

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def procesando():
    if not Encuestado.validate_encuestado(request.form):
        return redirect('/')
    data={
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "ubicacion":request.form['ubicacion'],
        "lenguaje":request.form['lenguaje'],
        "comentario":request.form['comentario'],
        "genero": request.form['genero'], 
        "terminos":request.form['terminos'],
    }
    print(data)
    nuevo_encuestado=Encuestado.creardojo(data)
    print(nuevo_encuestado)
    #Esto es porque el checkbox solo da "on" como información, entonces para traspasarla a la tabla de manera mas coherente
    return redirect(f"/encuestado/{nuevo_encuestado}")

@app.route('/encuestado/<int:num>')
def un_encuestado(num):
    data={
        "id":num
    }
    encuestado= Encuestado.un_encuestado(data)
    print(encuestado)
    return render_template('resultado.html', encuestado=encuestado)

@app.route('/volver',methods=['POST'])
def volver():
    return redirect('/')