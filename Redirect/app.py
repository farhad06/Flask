from flask import Flask,request,render_template,url_for,redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("login.html")
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin':
        return redirect(url_for('success'))
    else:
        name=request.form['username']
        return redirect(url_for('user',name=name))
@app.route('/success')
def success():
    return "<center><h1>Successfully logged in</h1></center>"
@app.route('/guest')
def guest():
    return "<center><h1>Enter correct username</h1></center>"
@app.route('/user',methods=['GET','POST'])
def user():
    return render_template('user.html',name=request.args['name'])
if __name__=='__main__':
    app.run(debug=True)