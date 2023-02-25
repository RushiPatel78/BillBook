# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import *
import os
#import pyrebase

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/invoiceforapproval')
def invoiceforapproval():
    return render_template('invoiceforapproval.html')
    
@app.route('/addclient')
def addclient():
    return render_template('addclient.html')

@app.route('/clientlist')
def clientlist():
    return render_template('clientlist.html')

@app.route('/removeclient')
def removeclient():
    return render_template('removeclient.html')

@app.route('/addproject')
def addproject():
    return render_template('addproject.html')

@app.route('/projectlist')
def projectlist():
    return render_template('projectlist.html')

@app.route('/removeproject')
def removeproject():
    return render_template('removeproject.html')

     


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
