import cv2
from cvzone.FaceMeshModule import FaceMeshDetector as Fd


cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

detector = Fd(maxFaces=2)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
    #     pass
    cv2.imshow("Image", img)
    cv2.waitKey(1)