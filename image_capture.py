import numpy as np
import cv2 
import cv2.aruco as aruco
import math
import requests
import imutils

url = "https://192.168.29.186:8080/shot.jpg"
#cap = cv.VideoCapture(url)
#frames_per_second = int(cap.get(cv.CAP_PROP_FPS))
#print(frames_per_second)

while True:
    img_resp = requests.get(url,verify = False)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)




    #ret, frame = cap.read()
    #frames_per_second = int(cap.get(cv.CAP_PROP_FPS))
    #print(frames_per_second)
    #if frame is not None:
    #    cv.imshow('frame', frame)
#
    if cv2.waitKey(1) == ord('q'):
        break

    dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_250) #provide the predefined dictionary that will be used
    parameter = aruco.DetectorParameters() #provide detector parameters
    detector = aruco.ArucoDetector(dictionary,parameter)

    (corners, id, rejected) = detector.detectMarkers(img)

    if id is not None:
        print(corners)
        #aruco.drawDetectedMarkers(img,corners,id) #draws a box around the aruco
        #arr = np.array(corners)
        #x1=arr[0][0]
        #x3=arr[2][0]
        #y1=arr[0][1]
        #y3=arr[2][1]
        #x_center=(x1+x3)/2
        #y_center=(y1+y3)/2

        #globalvariable.x_obj = x_center - 320
        #globalvariable.y_obj = 240 - y_center
        #print(globalvariable.x_obj, globalvariable.y_obj)

    else:
        continue
    #cv2.imshow("out",img)


#cap.release()
cv2.destroyAllWindows()