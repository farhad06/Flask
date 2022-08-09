from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def fun():
    return "<h1>This function running in App2</h1>"
@app.route('/aboutus')
def about_us():
    return "<p>This is my contact number <br> <h2> 9609387445 </h2></p>"
@app.route('/admin')
def admin():
    return "Hello Admin"
@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s !" %guest
@app.route('/hello/<name>')
def hello(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
if __name__=='__main__':
    app.run(port=5001,debug=True)