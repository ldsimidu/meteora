from flask import Flask, render_template, request, redirect, url_for
from db_editors.addtab_pessoas_db import *
from db_editors.remtab_pessoas_db import *
from prettytable import PrettyTable
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    pessoas = view_pessoas.fetchall()
    return render_template('templeates.index.html', pessoas=pessoas)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        email = request.form['email']
        telefone = request.form['telefone']
        genero = request.form['genero']
        
        cursor.execute("INSERT INTO pessoas (nome, idade, email, telefone, Genero) VALUES (?, ?, ?, ?, ?)", (nome, idade, email, telefone, genero))
        banco_meteora.commit()
        
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id_exc = request.form['id']
        
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_exc,))
        banco_meteora.commit()

        return redirect(url_for('index'))
    
    pessoas = view_pessoas.fetchall()
    return render_template('delete.html', pessoas=pessoas)


