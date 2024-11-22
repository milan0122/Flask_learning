from flask import Flask, render_template,Response
import cv2
import face_recognition
import numpy as np
import time
app = Flask(__name__)

camera = cv2.VideoCapture(0)
# eye_detect = cv2.CascadeClassifier('/Users/milandangi/Desktop/Flask_learning/Face_detection_project/Haarcascades/haarcascade_eye_tree_eyeglasses.xml')
# face_detect = cv2.CascadeClassifier('/Users/milandangi/Desktop/Flask_learning/Face_detection_project/Haarcascades/haarcascade_frontalface_default.xml')
#load the images
milan_image = face_recognition.load_image_file("/Users/milandangi/Desktop/Projects/Python Project/Flask_learning/Face_detection_project/Images/milan.jpg")
milan_face_encoding = face_recognition.face_encodings(milan_image)[0]

samir_image = face_recognition.load_image_file("/Users/milandangi/Desktop/Projects/Python Project/Flask_learning/Face_detection_project/Images/samir.jpeg")
samir_face_encoding = face_recognition.face_encodings(samir_image)[0]
bibas_image = face_recognition.load_image_file("/Users/milandangi/Desktop/Projects/Python Project/Flask_learning/Face_detection_project/Images/bibas.JPG")
bibas_face_encoding = face_recognition.face_encodings(bibas_image)[0]
aa_image = face_recognition.load_image_file("/Users/milandangi/Desktop/Projects/Python Project/Flask_learning/Face_detection_project/Images/aarosi.jpeg")
aa_face_encoding = face_recognition.face_encodings(aa_image)[0]

#create arrays of known face encoding and their names
known_face_encodings=[
    milan_face_encoding,
    samir_face_encoding,
    bibas_face_encoding,
    aa_face_encoding
]
known_face_names = [
    "Milan Dangi",
    "Samir Dangi",
    "Bibas Dangi",
    "Aarosi Oli"
]
#initialize some variables
face_locations = []
face_encodings=[]
face_names = []
process_this_frame = True
def generate_frames():
    #read the camera frame
    while True:
        sucess,frame=camera.read()
        if not sucess:
            break
        else:
            #resize the frame of video 1/4 size for faster face recognition
            small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

            #convert the image from BGR color to RGB
            rgb_small = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
            #only process the face and face encoding in the current frame
            if process_this_frame:
                #find all the faces and face encoding in the current frame
                face_locations = face_recognition.face_locations(rgb_small)
                face_encodings = face_recognition.face_encodings(rgb_small,face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    #see if the face is match for the known face
                    matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
                    name = "Unkown"

                    #use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    face_names.append(name)
                for(top,right,bottom,left), name in zip(face_locations,face_names):
                    #scale back up face location 
                    top *=4
                    right *=4
                    bottom *=4
                    left *=4

                    # Draw a box around the face
                    cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),2)
                    cv2.rectangle(frame,(left,bottom-40),(right,bottom),(0,0,255),cv2.FILLED )
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)

                # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                # face = face_detect.detectMultiScale(gray,1.3,5)
            
            
                # for (x,y,w,h) in face:
                #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                #     roi_gray = gray[y:y+h,x:x+w]
                #     roi_color = frame[y:y+h,x:x+w]
                #     eyes = eye_detect.detectMultiScale(roi_gray,1.1,3)
                #     for (ex,ey,ew,eh) in eyes:
                #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


            sucess,buff=cv2.imencode('.jpg',frame)
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
