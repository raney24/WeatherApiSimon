from flask import Flask, render_template, redirect, url_for, request
from string import Template
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/hello/<name>/")
def hello_name(name):
    return render_template('index.html', name = name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method =='POST':
        user = request.form['nm']
        return redirect(url_for('hello_name',name = user)) 
    else:
        user = request.args.get('nm') if request.args.get('nm') else 'No user'
        return redirect(url_for('hello_name',name = user))
    

if __name__ == "__main__":
    app.run(debug = True)

