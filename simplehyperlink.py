#importing
from flask import Flask,render_template
#interaction
app = Flask(__name__)
#mapping
@app.route('/')
#input
def home():
    return render_template('home.html')
@app.route('/secondpage')
def about():
    return "This is 2nd Page"
#main
if __name__=='__main__':
    app.run(debug=True)