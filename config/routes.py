from flask import Blueprint, render_template

bp = Blueprint('routes', __name__,template_folder=os.path.join(os.getcwd(), '../views'))


@bp.route("/")
def index():
     datos_r = {
            'titulo':'Datos desde el controlar de python',
            'contenido': 'Datos con python'
        }
    return render_template('index.html', datos_r=datos_r)