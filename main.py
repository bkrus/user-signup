from flask import Flask, request, redirect, render_template
import cgi
import os
import string



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_index():
    return render_template('index.html')

def is_empty (n): #Check if a string is empty
        if n == "":
            return True

def is_char(letters): #Check if letters in a string do not contain spaces or special characters
    for i in letters.lower:
        if i in string.ascii_lowercase:
            return True

@app.route('/', methods=['post'])
def validate_index():
    username = request.form['username']
    username_error= ''

    password = request.form['password']
    password_error= ''
    password_length=''

    verify = request.form['verify']
    verify_error= ''
    
    #Username validations
    if is_empty (username): 
        username_error = 'Username cannot be empty'
        username = ''
    #Password validations
    if is_empty(password): 
            password_error = 'Password cannot be empty'
            password = ''
    
    if len(password) < 3 and len(password) >20:
        password_error = 'Password must be between 3 and 20 characters'
        password = ''
    
    else: 
        if not is_char(password):
            password_error = 'Password can only contain letters'
            password = ''

    #Verify Password Validations   
    if is_empty(verify):
        verify_error = ' Verify Password cannot be empty'
        verify = '' 
    
    if verify != password:
        verify_error = ' Verify Password must match Password'
        verify = '' 
            
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error)
    
    else:
        return render_template('welcome.html', username=username)
     

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()