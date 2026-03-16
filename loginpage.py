#importing
from flask import Flask
from flask import render_template
from flask import request

#interaction

web=Flask(__name__)

#mapping
@web.route('/')
@web.route('/register')

#input
def homepage():
    return render_template('register.html')

#mapping
@web.route('/confirmation',methods=['GET','POST'])
def register():
    if request.method=='POST':
        n=request.form.get('name')
        e=request.form.get('email')
        p=request.form.get('phone')
    return render_template('confirm.html',name=n,email=e,phone=p)

#main
if __name__ == '__main__':
    web.run(debug=True)
