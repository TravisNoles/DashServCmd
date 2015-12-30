from flask import Flask, url_for, render_template

@app.route('/')
def viewDashboard():
    return "Not implemented."

@app.route('/settings')
def viewSettings():
    return "Not implemented."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
