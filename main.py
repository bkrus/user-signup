from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_index():
    return render_template('index.html')

def is_empty (n):
        if n == "":
            return True

@app.route('/', methods=['post'])
def validate_index():
    username = request.form['username']
    username_error= ''

    password = request.form['password']
    password_error= ''

    verify = request.form['verify']
    verify_error= ''
    
    if is_empty (username):
        username_error = 'Username cannot be empty'
        username = ''
        
        #return render_template('index.html', username_error=username_error)

    if is_empty(password):
        password_error = 'Password cannot be empty'
        password = ''
    
    if is_empty(verify):
        verify_error = ' Verify Password cannot be empty'
        verify = ''   
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error)
    
    else:
        return render_template('welcome.html', username=username)
     

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()