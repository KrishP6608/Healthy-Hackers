import cv2
cam =cv2.VideoCapture(0)

while True:
    _, frame = cam.read
    frame =cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(0) == 27:
        break

cam.release()
cv2.destoryAllWindows()