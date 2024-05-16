from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        datos = {
            "apellidos": request.form['apellidos'],
            "nombre": request.form['nombre'],
            "fecha": request.form['fecha'],
            "hora": request.form['hora'],
            "centro": request.form['centro'],
            "email": request.form['email'],
            "userAgent": request.headers.get('User-Agent'),
            "ipAddress": request.remote_addr
        }
        # Guardar los datos en un archivo JSON
        with open('datos_usuarios.json', 'a') as f:
            json.dump(datos, f)
            f.write('\n')
        return redirect(url_for('agradecimiento'))

@app.route('/agradecimiento')
def agradecimiento():
    return render_template('agradecimiento.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
