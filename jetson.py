import numpy as np
import cv2
import time
wcam , hcam = 720,480
face_cascade = cv2.CascadeClassifier('C:/Users/roni/PycharmProjects/pythonProject/Test/loc.xml')

ptime = 0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=30/1 ! nvvidconv flip-method='+str(flip)+ ' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap = cv2.VideoCapture(camSet)

cap.set(3,wcam)
cap.set(4,hcam)

while True:
    ret, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_180)
    img = cv2.resize(img, (wcam, hcam))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    deect = face_cascade.detectMultiScale(gray,  scaleFactor=1.40,
                minNeighbors=3,
                )
    v = len(deect)
    for (x, y, width, height) in deect:
        cv2.rectangle(img, (x,y), (x+width, y+height ), (0,0,255), 5)
        cv2.putText(img, "bird: " + str(v),(20, 50),0,2,(100,200,0), 3)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f'FPS: {int(fps)}', (420, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow('realtimebird', img)

    if cv2.waitKey(1) & 0Xff == ord('q'):  # press q to exit
        break_flag = True
        break

cap.release()
cv2.destroyWindow()