#integrating html with flask 
##HTTP get and post
from flask import Flask,redirect,request,url_for,render_template

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
@app.route('/sucess/<int:score>')
def sucess(score):
   result =""
   if score >= 50:
      result = "pass"
   else:
      result = "fail"
   return render_template('result.html',result =result)
   #return "Congratulations,You passed the exam"
# @app.route('/fail/<int:score>')
# def fail(score):
#    return "You failed in exam, better for next time"
##Result checker
@app.route('/submit',methods=['POST','Get'])
def submit():
   total_score = 0
   if request.method=='post':
      science = float(request.form['Science'])
      math = float(request.form['Math'])
      Cprog = float(request.form['C programming'])
      English = float(request.form['English'])
      Nepali = float(request.form['Nepali'])
      total_score = (science + math + Cprog + English + Nepali)/5


   result = ""
   if total_score >= 50:
      result = "sucess"
   return redirect(url_for(result,score = total_score))

if __name__=='__main__':
   app.run(debug=True)