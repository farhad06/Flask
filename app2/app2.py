from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def student():
    return render_template("student_marks.html")
@app.route('/data',methods=['POST','GET'])
def data():
    if request.method=="POST":
        result=request.form
        return render_template("result.html",result=result)

if __name__=="__main__":
    app.run(port=1005,debug=True)