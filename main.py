from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def is_empty (input):
    if input == '':
        return True

@app.route('/')
def display_index():
    return render_template('index.html')

@app.route('/', methods=['post'])
def validate_index():
    username = request.form['username']
    username_error= ''
    
    if is_empty(username) == True:
        username_error = 'Username cannot be empty'
        username = ''
        return render_template('index.html', username_error=username_error)
    else:
        return render_template('welcome.html', username=username)
     

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()