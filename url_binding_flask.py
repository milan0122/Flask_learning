## binding url dynamically
# variable rules and url building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome1():
    return "Welcome to my home"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "The person passed and marks is " + str(score)
##result checker
@app.route('/result/<int:marks>')
def results(marks):
    results = ""
    if marks < 50:
        results = 'fail'
    else:
        results = 'sucess'
    return redirect(url_for(results,score=marks))


@app.route('/fail/<int:score>')
def fail(score):
    return "The person failed and marks is " + str(score)



if __name__=='__main__':
    app.run(debug=True)