import cv2
from cvzone.FaceMeshModule import FaceMeshDetector as Fd
import os
import random
import cvzone

from objectsimport import ObjectsImport
from camera import Camera

class Game:
    def __init__(self):
        self.speed = 10
        self.count = 0
        self.isEatable = True
        self.gameOver = False
        self.mouthId = [0,17,78,292]
        self.pos = [300, 0]
        self.currentObject = None
        self.cap = None
        self. eatables = None
        self. noneatables = None
        self.img = None
        self.face = []
        self.faces = []
        self.up = []
        self.down = []
        self.upDown = []
        self.leftRight = None
        self.distMounthObject = None
        self.ratio = None
        self.key = ""
    
    def initialize(self,type: str = "fruits"):
        self.cap = Camera().start()
        self.eatables = ObjectsImport().importobjects(type=type)
        self.noneatables = ObjectsImport().importobjects()
        while self.img is None:
            self.img = self.cap.read()
        self.resetobject()

    def resetobject(self):
        self.pos[0] = random.randint(50,self.cap.width())
        self.pos[1] = 10
        randNo = random.randint(0,2)
        if randNo == 0:
            i = random.randint(0,len(self.noneatables)-1)
            self.currentObject = self.noneatables[i]

            self.isEatable = False
        else:
            i = random.randint(0,len(self.noneatables)-1)
            self.currentObject = self.eatables[i]

            self.isEatable = True
        
        # frutas = ["manzana","mango","piña","platano","uva","naranja","sandia","fresa"]
        # nocomestibles = ["bomba","Laptop","raton","silla"]
        # if randNo == 0: print(f'no comestible, {nocomestibles[i]}, shape = {np.shape(self.currentObject)}')
        # else: print(f'comestible, {frutas[i]}, shape = {np.shape(self.currentObject)}')

    def facesDetect(self):
        self.img,self.faces = self.cap.detector.findFaceMesh(self.img, draw=False)
        if self.faces:
            self.face = self.faces[0]
            self.up = self.face[self.mouthId[0]]
            self.down = self.face[self.mouthId[1]]
            for id in self.mouthId:
                    cv2.circle(self.img,self.face[id],1,(255, 0, 255),5)                    
    
    def distance(self):
        if len(self.face) == 0: return
        self.upDown,_ = self.cap.detector.findDistance(self.face[self.mouthId[0]],self.face[self.mouthId[1]])
        self.leftRight,_ = self.cap.detector.findDistance(self.face[self.mouthId[2]],self.face[self.mouthId[3]])
        

    def objectDistance(self):
        if len(self.face) == 0: return
        cx,cy = (self.up[0]+self.down[0])//2,(self.up[1]+self.down[1])//2
        self.distMounthObject,_ = self.cap.detector.findDistance((cx,cy),(self.pos[0]+50,self.pos[1]+50))

    def isOpen(self):
        if (self.upDown is None or self.leftRight is None): return
        self.ratio = int((self.upDown/self.leftRight)*100)

    def eat(self):
        if (self.distance is None or self.ratio is None): return
        if self.distMounthObject<75 and self.ratio > 70:
            if self.isEatable:
                self.resetobject()
                self.count += 1
            else:
                self.gameOver = True
                cv2.putText(self.img,"Fin del juego",(int(self.cap.width()/4),int(self.cap.height()/2)),cv2.FONT_HERSHEY_COMPLEX,2,(255, 0, 255),5)

    def loop(self,type: str = "fruits"):
        self.initialize(type=type)
        while True:
            if self.gameOver is False:
                try:
                    self.img = self.cap.read()
                    cv2.putText(self.img,str(self.count),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255, 0, 255),5)
                    self.img = cvzone.overlayPNG(self.img,self.currentObject,self.pos)
                except: pass
                self.pos[1] += self.speed
                if self.pos[1]>(self.cap.height()-50): self.resetobject()
                self.facesDetect()
                self.distance()
                self.objectDistance()
                self.isOpen()
                self.eat()
            cv2.imshow("Image",self.img)
            self.key = cv2.waitKey(1)
            if self.key == ord("r"):
                self.resetobject()
                self.gameOver = False
                self.count = 0
            elif self.key == ord("q"): break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    game = Game().loop()