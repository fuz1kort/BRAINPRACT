import cv2

# img = cv2.imread('C:/Users/Marat/Pictures/image.png')
# cv2.imshow('Result', img)
#
# cv2.waitKey(0)

# cap=cv2.VideoCapture("C:/Users/Marat/Videos/Counter-strike  Global Offensive/Counter-strike  Global Offensive 2021.05.03 - 09.28.55.02.mp4")
cap = cv2.VideoCapture(0) #Первая вебка 1901 коммит
cap.set(3, 500)
cap.set(4, 800)

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
