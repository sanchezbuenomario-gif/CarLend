import os
import random
import sqlite3
from flask import Flask, render_template, jsonify, request, redirect, url_for
from models.vehiculosModel import VehiculoModel
from scripts.crear_db import crear_base_datos
from controllers.flotaController import register_flota_routes

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    crear_base_datos()
    
    register_flota_routes(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/registro', methods=['GET','POST'])
    def registro():
        if request.method == 'POST':

            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']
            telefono = request.form['telefono']

            conn = sqlite3.connect('instance/carlend.db')
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO usuarios (nombre,email,password,telefono)
            VALUES (?,?,?,?)
            """,(nombre,email,password,telefono))

            conn.commit()
            conn.close()

            return redirect(url_for('cliente'))

        return render_template('registro.html')

    @app.route('/seguro') 
    def seguro(): return render_template('seguro.html')

    @app.route('/cliente') 
    def cliente(): return render_template('cliente.html')

    @app.route('/alquiler') 
    def alquiler(): return render_template('alquiler.html')

    @app.route('/metodos-pago') 
    def metodos_pago(): return render_template('metodos-pago.html')

    @app.route('/mis-reservas') 
    def mis_reservas(): return render_template('mis-reservas.html')

    @app.route('/faq') 
    def faq(): return render_template('faq.html')

    @app.route('/privacidad') 
    def privacidad(): return render_template('privacidad.html')

    @app.route('/seguridad') 
    def seguridad(): return render_template('seguridad.html')

    @app.route('/documentacion') 
    def documentacion(): return render_template('documentacion.html')

    @app.route('/sedes') 
    def sedes(): return render_template('sedes.html')

    @app.route('/admin') 
    def admin(): return render_template('admin.html')

    return app