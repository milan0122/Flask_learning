from flask import Flask, render_template,Response
import cv2
import time
app = Flask(__name__)

camera = cv2.VideoCapture(0)
eye_detect = cv2.CascadeClassifier('/Users/milandangi/Desktop/Flask_learning/Face_detection_project/Haarcascades/haarcascade_eye_tree_eyeglasses.xml')
face_detect = cv2.CascadeClassifier('/Users/milandangi/Desktop/Flask_learning/Face_detection_project/Haarcascades/haarcascade_frontalface_default.xml')

def generate_frames():
    #read the camera frame
    while True:
        sucess,frame=camera.read()
        if not sucess:
            break
        else:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face = face_detect.detectMultiScale(gray,1.3,5)
            
            for (x,y,w,h) in face:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_color = frame[y:y+h,x:x+w]
                eyes = eye_detect.detectMultiScale(roi_gray,1.1,3)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


            ret,buff=cv2.imencode('.jpg',frame)
            frame=buff.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')
        time.sleep(0.01)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__=="__main__":
    app.run(debug=True)
