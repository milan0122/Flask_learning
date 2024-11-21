from flask import Flask
#WSGI application which is standard application to communicate between web server and web application
app= Flask(__name__)

#decorator 
@app.route('/')
def welcome():
 return "Hello Milan, How are you"

@app.route("/music")
def music():
 return "Playing music"


if __name__=='__main__':
 app.run(debug=True)#debug true helps to reload after changes