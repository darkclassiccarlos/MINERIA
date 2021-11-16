import pandas as pd
from flask import Flask, render_template
from flask.json import jsonify
from flask import Response
from users import users
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory


####
#### VARIABLES PARA IDENTIFICAR EL ALMACENAMIENTO DEL ARCHIVO 
UPLOAD_FOLDER = '/Users/carlosbautista/Desktop/Maestría/Mineria de datos/ProyectEDAs/MINERIA/files'
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # comprueba si la solicitud de la peticion tiene el archivo
        if 'file' not in request.files:           
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/readcsv', methods=['GET'])
def read():
    filename = '/Users/carlosbautista/Desktop/Maestría/Mineria de datos/ProyectEDAs/MINERIA/files/prueba.csv'

    data = pd.read_csv(filename, header= None)
    myData = data.values
    print(myData)
    return render_template('home.html', myData=myData)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug = True)
    app.config['SESSION_TYPE']='filesystem'