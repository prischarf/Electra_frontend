'''
  Backend para el Frontend usado en Electra para ejecutar APIs
'''

import hashlib
from flask import Flask, request, render_template, session
import pandas as pd

# Como estás dentro de la carpeta PAGINA_WEB, solo usás los nombres directos
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "una_clave_secreta_segura"

def hash_password(password):
    """
    Genera el hash SHA-256 de una contraseña.
    """
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    """
    Renderiza la página de inicio.
    """
    return render_template('Index.html')

@app.route('/login_admin')
def login_admin():
    """
    Renderiza la vista de login para usuarios de administración.
    """
    return render_template('Login_Admin.html')

@app.route('/login_compras')
def login_compras():
    """
    Renderiza la vista de login para usuarios de compras.
    """
    return render_template('Login_Compras.html')

@app.route('/iniciar_admin', methods=['POST'])
def iniciar_admin():
    """
    Procesa el login del usuario del área de administración.
    Valida contra el archivo usuarios.xlsx y guarda el usuario en sesión.
    """
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contraseña')
    hash_contrasena = hash_password(contrasena)

    df = pd.read_excel('usuarios.xlsx')
    user_row = df[df['Usuario'] == usuario]

    if user_row.empty:
        return "Usuario no registrado"
    if user_row.iloc[0]['Hash Contraseña (SHA-256)'] != hash_contrasena:
        return "Contraseña incorrecta"

    session['usuario'] = usuario

    return "✔ /administracion"

@app.route('/iniciar_compras', methods=['POST'])
def iniciar_compras():
    """
    Procesa el login del usuario del área de compras.
    Valida contra el archivo usuarios.xlsx y guarda el usuario en sesión.
    """
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contraseña')
    hash_contrasena = hash_password(contrasena)

    df = pd.read_excel('usuarios.xlsx')
    user_row = df[df['Usuario'] == usuario]

    if user_row.empty:
        return "Usuario no registrado"
    if user_row.iloc[0]['Hash Contraseña (SHA-256)'] != hash_contrasena:
        return "Contraseña incorrecta"

    session['usuario'] = usuario

    return "✔ /compras"

@app.route('/administracion')
def administracion():
    """
    Renderiza la vista principal del área de administración.
    """
    return render_template('Administracion.html')

@app.route('/formulario_rg')
def formulario_rg():
    """
    Renderiza el formulario para enviar el reporte RG.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Stock_RG.html', usuario=usuario)

@app.route('/formulario_softland')
def formulario_softland():
    """
    Renderiza el formulario para enviar el reporte de stock Softland.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Stock_Softland.html', usuario=usuario)

@app.route('/compras')
def compras():
    """
    Renderiza la vista principal del área de compras.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Compras.html', usuario=usuario)

@app.route('/formulario_alertas')
def formulario_alertas():
    """
    Renderiza el formulario para configurar y enviar alertas.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Alertas.html', usuario=usuario)

@app.route('/formulario_combplanillas')
def formulario_combplanillas():
    """
    Renderiza el formulario para combinar planillas.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Comb_Planillas.html', usuario=usuario)

@app.route('/formulario_embarques')
def formulario_embarques():
    """
    Renderiza el formulario para generar reportes de embarques CBU.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Embarques_CBU.html', usuario=usuario)

@app.route('/formulario_kits')
def formulario_kits():
    """
    Renderiza el formulario para generar reportes de kits.
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Kits.html', usuario=usuario)

@app.route('/formulario_necplanta')
def formulario_necplanta():
    """
    Renderiza el formulario para reportar necesidades de planta (repuestos).
    """
    usuario = session.get('usuario', 'desconocido')
    return render_template('Form_Nec_Planta_Repuestos.html', usuario=usuario)

if __name__ == '__main__':
    print("Carpeta templates:", app.template_folder)
    app.run(debug=True)
