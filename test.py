import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Couldn't open")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: cnt receive")
        break
    
    
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()