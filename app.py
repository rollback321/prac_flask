from flask import Flask , jsonify, render_template, request
from controllers.mmain_controllers import Main_controllers
from config.basedatos import Basedatos
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'views'))
#app = Flask(__name__)

@app.route("/")
def index():    
    base_url = request.base_url
    main_controller = Main_controllers()
    datos_r = main_controller.obtener_registros()

    html1 = render_template('header_views.html', datos_r = datos_r, base_url = base_url)
    body = render_template('body.html')
    html2 = render_template('fooder_views.html', datos_r = datos_r, base_url = base_url)
    html = html1 + body + html2

    return html

@app.route('/get_data', methods=['POST'])
def get_data():
    conn = Basedatos()
    # if conn:
    conn = conn.conectar_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_edificios_cholets")
    datos = cursor.fetchall()
    
    cursor.close()
    conn.close()
    #conexion = conn.conectar_db()
    # else:
    #     print("Error de conexion")

    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    # Simulación de datos (puedes reemplazar esto con tu lógica real)
    data = {'message': nombre}
    
    return  jsonify(datos)
    #jsonify(data)

if __name__ == "__main__":
    app.run()