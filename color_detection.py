import cv2
import numpy as np

CAMERA_INDEX = 0
TUNING = False

def empty_callback(x):
    """
    Callback function required for creating trackbars.
    """
    pass

webcam = cv2.VideoCapture(CAMERA_INDEX)
if not webcam.isOpened():
    print("There was a problem trying to open the camera. Closing the program...")
    exit()

if TUNING:
    cv2.namedWindow("Tuning")
    cv2.resizeWindow("Tuning", 400, 300)
    cv2.createTrackbar("L - H", "Tuning", 100, 179, empty_callback)
    cv2.createTrackbar("L - S", "Tuning", 150, 255, empty_callback) 
    cv2.createTrackbar("L - V", "Tuning", 50, 255, empty_callback)  
    cv2.createTrackbar("U - H", "Tuning", 140, 179, empty_callback) 
    cv2.createTrackbar("U - S", "Tuning", 255, 255, empty_callback) 
    cv2.createTrackbar("U - V", "Tuning", 255, 255, empty_callback) 
    
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = webcam.read()
    if not ret:
        print("There was a problem capturing frames from the camera. Closing the program...")
        exit()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if TUNING:
        l_h = cv2.getTrackbarPos("L - H", "Tuning")
        l_s = cv2.getTrackbarPos("L - S", "Tuning")
        l_v = cv2.getTrackbarPos("L - V", "Tuning")
        u_h = cv2.getTrackbarPos("U - H", "Tuning")
        u_s = cv2.getTrackbarPos("U - S", "Tuning")
        u_v = cv2.getTrackbarPos("U - V", "Tuning")
        lower_bound = np.array([l_h, l_s, l_v])
        upper_bound = np.array([u_h, u_s, u_v])
    else:
        # Default color detection: Blue
        lower_bound = np.array([100, 150, 121])
        upper_bound = np.array([140,255,255]) 

    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours: 
        if cv2.contourArea(contour) > 300:
            x, y, w, h = cv2.boundingRect(contour)   
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Color Detector", frame)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

webcam.release()
cv2.destroyAllWindows()
