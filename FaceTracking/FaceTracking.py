import cv2 
import numpy as np 

# Now calculate meanshift algorithms 
# meanshift algorithms is base object tracking 

# First calculate face detecting algorthmis and open video frame 
cap = cv2.VideoCapture(0)
ret , frame = cap.read()

features = cv2.CascadeClassifier('add xml file in your installition directory ')

detecting = features.detectMultiScale(frame)

# And first face detecting  calculate on  meanshift algorithms 
# So first face detetcting grap in detecting  and  define rectangle point  

(face_x,face_y,w,h) = tuple(detecting[0]) # this is first face detecting grab 

# And define track_window for meashift algorithms 
# track_window is first face detecting 

track_window = (face_x,face_y,w,h)

# Cut first face detecting area from frame 
cut_face = frame[face_y:face_y+h,face_x:face_x+w]

# And find hisotogram  in cut_face 
# So convert to HSV color 

cut_face_hsv = cv2.cvtColor(cut_face,cv2.COLOR_BGR2HSV)

cut_face_his = cv2.calcHist([cut_face_hsv],channels=[0],mask=None,histSize=[180],ranges=[0,180])

# And calculate cv2.normalize 
cv2.normalize(cut_face_his,cut_face_his,0,255,cv2.NORM_MINMAX)

# And calculate criteria 
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

# Now calculate meanshift aglorithms for frame 

while True:
    ret , frame = cap.read()
    if ret == True:
        
    
    # use calbackproject is calculated for meanshift aglorithms and change hsv color 
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        b = cv2.calcBackProject([hsv],[0],cut_face_his,[0,180],1)
    
    # Start meanshift algorithms calculate and meanshift algorithms is on  track_window calculate  
        ret , track_window = cv2.meanShift(b,track_window,criteria)
    
    # Now upload rectangle for see in frame 
        (x,y,w,h) = track_window
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),10)
    else:
        break
    cv2.imshow("rectangle " , img )
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
