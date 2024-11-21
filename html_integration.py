#integrating html with flask 
##HTTP get and post

#jinja2 template
'''
{%%} for statement
{{}} expression to print the statement
'''
from flask import Flask,redirect,request,url_for,render_template

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
   #return "Congratulations,You passed the exam"
# @app.route('/success/<int:score>')
# def success(score):
#    return render_template('result.html',result='pass',score=score)
# @app.route('/fail/<int:score>')
# def fail(score):
#    return render_template('result.html',result='fail',score=score)

# here we use the different api for two different condition pass and fail 
#likewise same condition can be done in html file using % expression % called jinja2 techniques
@app.route('/result_checker/<int:score>')
def result_checker(score):
   # return render_template('result.html',score=score)
   res =''
   if score >=50:
      res ='pass'
   else:
      res = 'fail'
   exp ={'score':score,'res':res}
   return render_template('result.html',result=exp)
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
   
   # if total_score >= 40:
   #    return redirect(url_for('success',score=total_score))
   
   # else:
   #    return redirect(url_for('fail',score=total_score))
      
      #here i comment out the if condition just the pass score

      return redirect(url_for("result_checker",score=total_score))
      
   

if __name__=='__main__':
   app.run(debug=True)