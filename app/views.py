from flask import render_template, flash, redirect, request, jsonify
from app import app
import logProcess

@app.route('/_add_numbers')
def add_numbers():
    user = request.args.get('a',0,type=str)
    x,y,usrM,idxM,sumy = logProcess.mainlog(user)
        
    return jsonify(result=[x,y,usrM,idxM,sumy])

@app.route('/')
def index():
    return render_template('addnum.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/about')
def about():
    return render_template('about.html')
