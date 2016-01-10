#This file runs dashservcmd.
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def gotoIndex():
    return render_template('base.html')

@app.route('/app')
def viewAppManager():
    return render_template('applications.html')

@app.route('/app/<app_name>/<action>')
def appAction(app_name, action):
    return "Commiting %s" % app_name

@app.route('/settings')
def viewSettings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
