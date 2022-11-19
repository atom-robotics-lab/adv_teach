import cv2
cap=cv2.VideoCapture("https://192.168.164.121:8080")
while True:
    ret,frame=cap.read()
    if ret == True:

        cv2.imshow("frame",frame)

        key = cv2.waitKey(10)
    cap.release()
    cv2.destroyAllWindows()
