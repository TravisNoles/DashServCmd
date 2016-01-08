#This file runs dashservcmd.
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def gotoIndex():
    return render_template('base.html')

@app.route('/app/manager')
def viewAppManager():
    return

@app.route('/app/install/<app_name>')
def installApp(app_name):
    return "Installing %s" % app_name

@app.route('/settings')
def viewSettings():
    return "Not implemented."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
