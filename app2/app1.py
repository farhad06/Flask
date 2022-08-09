from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route('/hello/<user>')
def hello(user):
    return render_template('index.html',name=user)
@app.route('/result')
def res():
    dict={"Rohit":45,"Virat":18,"Pant":17,"Rahul":1}
    return render_template('index.html',result=dict)
if __name__=='__main__':
    app.run(debug=True)