import cv2
from cvzone.FaceMeshModule import FaceMeshDetector as Fd
import os
import random
import cvzone
from select_camera import screenVideo 

cap = screenVideo()
cap.set(3, 1280)
cap.set(4, 720)

detector = Fd(maxFaces=1)

# detect path
abspath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(abspath)

# import fruits
folderEatable = f'{fileDirectory}\\Objects\\eatable\\vegetables'
listEatable = os.listdir(folderEatable)
eatables = []
for object in listEatable:
    eatables.append(cv2.imread(f'{folderEatable}/{object}', cv2.IMREAD_UNCHANGED))

# import noneatable
folderNonEatable = f'{fileDirectory}\\Objects\\noneatable'
listNonEatable = os.listdir(folderNonEatable)
nonEatables = []
for object in listNonEatable:
    nonEatables.append(cv2.imread(f'{folderNonEatable}/{object}', cv2.IMREAD_UNCHANGED))

currentObject = eatables[0] #use the firts vegetable
pos = [300, 0] # first non-random position
speed = 8
count = 0
global isEatable
isEatable = True
gameOver = False

def resetObject():
    global isEatable
    pos[0] = random.randint(100, 1000)
    pos[1] = 0
    randNo = random.randint(0, 2)
    if randNo == 0:
        currentObject = nonEatables[random.randint(0, 3)]
        isEatable = False
    else:
        currentObject = eatables[random.randint(0, 7)]
        isEatable = True
    return currentObject

idList = [0,17,78,292] ## mouth detection

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)

    if gameOver is False:
        img, faces = detector.findFaceMesh(img, draw=False)

        img = cvzone.overlayPNG(img, currentObject, pos)
        pos[1] += speed
        # print(pos[0],pos[1])

        if pos[1] > 600:
            currentObject = resetObject()

        if faces:
            face = faces[0]

            up = face[idList[0]]
            down = face[idList[1]]

            for id in idList:
                cv2.circle(img, face[id], 1, (255, 0, 255), 5)

            upDown, _ = detector.findDistance(face[idList[0]], face[idList[1]])
            leftRight, _ = detector.findDistance(face[idList[2]], face[idList[3]])

            ## Distance of the Object
            cx, cy = (up[0] + down[0]) // 2, (up[1] + down[1]) // 2
            distMouthObject, _ = detector.findDistance((cx, cy), (pos[0] + 50, pos[1] + 50))

            # opened or closed ratio
            ratio = int((upDown / leftRight) * 100)
            #
            if distMouthObject < 100 and ratio > 60:
                if isEatable:
                    currentObject = resetObject()
                    count += 1
                else:
                    gameOver = True
        cv2.putText(img, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 5)
    else:
        cv2.putText(img, "Fin del juego", (300, 400), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 255), 10)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('r'): ## reset the game
        resetObject()
        gameOver = False
        count = 0
        currentObject = eatables[0]
        isEatable = True
    elif key == ord('q'): ## quit the game
        break