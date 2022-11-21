import cv2

path = 'haarcascade_frontalface_default.xml'


cascade = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)

while True:
    isTrue, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    faces = cascade.detectMultiScale(gray, 1.2, 4)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,255), 2)

    cv2.imshow('Detection Face', img)

    cv2.waitKey(1)