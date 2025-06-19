'''
  Backend para el Frontend usado en Electra para ejecutar APIs
'''

import hashlib
from flask import Flask, request, render_template
import pandas as pd

# Como estás dentro de la carpeta PAGINA_WEB, solo usás los nombres directos
app = Flask(__name__, template_folder='templates', static_folder='static')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/login_admin')
def login_admin():
    return render_template('Login_Admin.html')

@app.route('/login_compras')
def login_compras():
    return render_template('Login_Compras.html')

@app.route('/iniciar_admin', methods=['POST'])
def iniciar_admin():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contraseña')
    hash_contrasena = hash_password(contrasena)

    df = pd.read_excel('usuarios.xlsx')
    user_row = df[df['Usuario'] == usuario]

    if user_row.empty:
        return "Usuario no registrado"
    if user_row.iloc[0]['Hash Contraseña (SHA-256)'] != hash_contrasena:
        return "Contraseña incorrecta"

    return "✔ /administracion"

@app.route('/iniciar_compras', methods=['POST'])
def iniciar_compras():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contraseña')
    hash_contrasena = hash_password(contrasena)

    df = pd.read_excel('usuarios.xlsx')
    user_row = df[df['Usuario'] == usuario]

    if user_row.empty:
        return "Usuario no registrado"
    if user_row.iloc[0]['Hash Contraseña (SHA-256)'] != hash_contrasena:
        return "Contraseña incorrecta"

    return "✔ /compras"

@app.route('/administracion')
def administracion():
    return render_template('Administracion.html')
@app.route('/formulario_rg')
def formulario_rg():
    return render_template('Form_Stock_RG.html')

@app.route('/formulario_softland')
def formulario_softland():
    return render_template('Form_Stock_Softland.html')

@app.route('/compras')
def compras():
    return render_template('Compras.html')

@app.route('/formulario_alertas')
def formulario_alertas():
    return render_template('Form_Alertas.html')

@app.route('/formulario_combplanillas')
def formulario_combplanillas():
    return render_template('Form_Comb_Planillas.html')

@app.route('/formulario_embarques')
def formulario_embarques():
    return render_template('Form_Embarques_CBU.html')

@app.route('/formulario_kits')
def formulario_kits():
    return render_template('Form_Kits.html')

@app.route('/formulario_necplanta')
def formulario_necplanta():
    return render_template('Form_Nec_Planta_Repuestos.html')

if __name__ == '__main__':
    print("Carpeta templates:", app.template_folder)
    app.run(debug=True)
