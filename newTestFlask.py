#importing

from flask import Flask

#interaction

web=Flask(__name__)

#mapping
@web.route('/')
@web.route('/home')

#input
def home():
    return "Welcome to Pani Corporation"

#main
if __name__ == '__main__':
    web.run(debug=True)
