'''
 sdasa
'''
# run_waitress.py
from waitress import serve
from PAGINA_WEB.app import app  # Importa tu instancia de Flask desde app.py

if __name__ == "__main__":
    print("Corriendo Flask con Waitress en http://0.0.0.0:5003 y ya veremos si anda...")
    serve(app, host="0.0.0.0", port=5003, threads=4)
