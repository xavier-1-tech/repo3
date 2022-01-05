from flask import Flask
from flask import render_template, g, redirect, request
from flask.helpers import url_for
import sqlite3
import os

currentlocation = os.path.dirname(os.path.abspath(__file__))

application = app = Flask(__name__)

#Flask Code
@app.route('/')
def quest():
    return render_template('index.html')

@app.route('/index.html')
def quest10():
    return render_template("index.html")    

@app.route('/doctor-list.html')
def quest2():
    return render_template('doctor-list.html')

@app.route('/about.html')
def quest3():
    return render_template('about.html')

@app.route('/lab-add-patient.html')
def quest4():
    return render_template('lab-add-patient.html')

@app.route('/patient-history.html')
def quest5():
    return render_template('patient-history.html')

@app.route('/registration.html')
def quest6():
    return render_template('registration.html')

@app.route('/registration-lab.html')
def quest7():
    return render_template('registration-lab.html')

@app.route('/sign-in-doc.html', method = ["POST"])
def quest8():
    UN = request.form['username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentlocation + "\login.db")
    cursor = sqlconnection.cursor(0)
    query1 = "SELECT Username, Password From "

    return render_template('sign-in-doc.html')

@app.route('/sign-in-lab.html')
def quest9():
    return render_template('sign-in-lab.html')





if __name__ == "__main__":
    app.run()