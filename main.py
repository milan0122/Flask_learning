#integrating html with flask 
##HTTP get and post
from flask import Flask,redirect,request,url_for,render_template

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
   #return "Congratulations,You passed the exam"
@app.route('/success/<int:score>')
def success(score):
   return render_template('result.html',result='pass',score=score)
@app.route('/fail/<int:score>')
def fail(score):
   return render_template('result.html',result='fail',score=score)

##Result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
   total_score = 0
   if request.method=='POST':
      science = float(request.form['sc'])
      math = float(request.form['mth'])
      Cprog = float(request.form['cprog'])
      English = float(request.form['Eng'])
      Nepali = float(request.form['Nep'])
      total_score = (science + math + Cprog + English + Nepali)/5
   
   if total_score >= 40:
      return redirect(url_for('success',score=total_score))
   
   else:
      return redirect(url_for('fail',score=total_score))
      
   

if __name__=='__main__':
   app.run(debug=True)