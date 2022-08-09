from flask import Flask,render_template,request,redirect,url_for
import re

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home ():
    if request.method=="POST":
        string = request.form['test_string']
        match_string=request.form['reg_ex']
        count=re.findall(match_string,string)
        #return "There are {} {}".format(len(count),match_string)
        return render_template('index.html',cnt=len(count),reg=match_string)
    #return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)
