import numpy as np
import cv2 
import cv2.aruco as aruco
import math
import requests
import imutils
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Disable SSl Certificate warning

url = "https://192.168.29.186:8080/shot.jpg"
cap = cv2.VideoCapture(url)

global x_obj                #find the x coordiante of the centre 
global y_obj                #find the y coordiante of the centre

while True:
    frames_per_second = int(cap.get(cv2.CAP_PROP_FPS))
    #print(frames_per_second)                   #uncomment to see frames per second
    img_resp = requests.get(url,verify = False)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)

    if cv2.waitKey(1) == ord('q'):    #press q on the keyboard to exit the webcam
        break

    dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_250) #provide the predefined dictionary that will be used
    parameter = aruco.DetectorParameters()                         #provide detector parameters
    detector = aruco.ArucoDetector(dictionary,parameter)

    (corners, id, rejected) = detector.detectMarkers(img)

    if id is not None:
        print(corners)
        aruco.drawDetectedMarkers(img,corners,id) #draws a box around the aruco
        arr = corners
        #print(arr)                 #uncomment to print the arrray
        x1=arr[0][0][0][0]
        x3=arr[0][0][2][0]
        y1=arr[0][0][0][1]
        y3=arr[0][0][2][1]
        x_center=(x1+x3)/2          #Centre of the aruco x coordinate
        y_center=(y1+y3)/2          #centre of the aruco y coordinate

        x_obj = x_center - 320
        y_obj = 240 - y_center
        print(x_obj, y_obj)

    else:
        continue

cap.release()
cv2.destroyAllWindows()             #Close window once out of loop