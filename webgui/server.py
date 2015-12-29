from flask import Flask, url_for, render_template


@app.route('/')
def viewDashboard():
    return "Not implemented."

@app.route('/settings')
def viewSettings():
    return "Not implemented."
