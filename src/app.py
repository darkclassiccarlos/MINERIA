from flask import Flask, render_template
from flask.json import jsonify
from flask import Response
from users import users

####
#from flask_mysqldb import MySQL
####
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/users')
def userHandler():
    return jsonify({"users": users}) 

# @app.route('/add_contact')
# def add_contact():
#     return 'add contact'

# @app.route('/edit')
# def edit_contact():
#     return 'edit contact'

# @app.route('/delete')
# def delete():
#   return 'delete contact'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug = True)

