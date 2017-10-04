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
    for i in letters:
        if not i.isalpha():
            return False
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

    email = request.form['email']
    email_error= ''
    
    #Username validations
    if is_empty(username): 
        username_error = 'Username cannot be empty'

    #Password validations
    if is_empty(password): 
            password_error = 'Password cannot be empty'
    
    if len(password) < 3 or len(password) >20:
        password_error = 'Password must be between 3 and 20 characters'
        password = ''
    
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
    
    #email validatations
    if not is_empty(email): 
        if '@' not in email:
            email_error = 'Email is not valid'
            email = ''
        
        if '.' not in email:
            email_error = 'Email is not valid'
            email = ''
        
        if len(email) < 3 or len(email) >20:
            email_error = 'Email is not valid'
            email = ''
        
        if email.count('@') > 1:
            email_error = 'Email is not valid'
            email = ''
        
        if email.count('.') > 1:
            email_error = 'Email is not valid'
            email = ''
    
    #render screen with error messages
    if username_error or password_error or verify_error or email_error:
        return render_template('index.html', 
                                username=username, 
                                email=email, 
                                username_error=username_error, 
                                password_error=password_error, 
                                verify_error=verify_error, 
                                email_error=email_error)
    #render Welcome 
    else:
        return render_template('welcome.html', username=username)
     

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()