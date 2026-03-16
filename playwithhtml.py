#importing

from flask import Flask
from flask import render_template

#interaction

web=Flask(__name__)

#mapping
@web.route('/')
@web.route('/register')

#input
def homepage():
    return render_template('register.html')

#main
if __name__ == '__main__':
    web.run(debug=True)
