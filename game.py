import cv2
import random
import numpy as np

from objectsimport import ObjectsImport
from camera import Camera

class Game:
    def __init__(self,dificult):
        self.dificult = dificult
        self.speed = 5
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
        self.up = []
        self.down = []
        self.upDown = []
        self.leftRight = None
        self.distMounthObject = None
        self.ratio = None
    
    def initialize(self,type: str = "fruits"):
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

    def mouthdetection(self):
        self.face = self.cap.detector.findFace(self.img)
        if self.face:
            self.up = self.face[self.mouthId[0]]
            self.down = self.face[self.mouthId[1]]
            for id in self.mouthId:
                    if self.ratio is not None:
                        if self.ratio > 65:
                            cv2.circle(self.img,self.face[id],1,(124,252,0),2)                    
                        else: cv2.circle(self.img,self.face[id],1,(255, 0, 255),2)                    
    
    def distance(self):
        if len(self.face) == 0: return
        self.upDown = self.cap.detector.findDistance(self.face[self.mouthId[0]],self.face[self.mouthId[1]])
        self.leftRight = self.cap.detector.findDistance(self.face[self.mouthId[2]],self.face[self.mouthId[3]])
        

    def objectDistance(self):
        if len(self.face) == 0: return
        x,y = (self.up[0]+self.down[0])//2,(self.up[1]+self.down[1])//2
        self.distMounthObject = self.cap.detector.findDistance((x,y),(self.pos[0]+50,self.pos[1]+50))

    def isOpen(self):
        if (self.upDown is None or self.leftRight is None): return
        self.ratio = int((self.upDown/self.leftRight)*100)

    def eat(self):
        if (self.distance is None or self.ratio is None): return
        if self.distMounthObject<70 and self.ratio > 65:
            if self.isEatable:
                self.resetobject()
                self.count += 1
                if self.dificult == 1: self.speed=self.speed+1
                elif self.dificult == 2: self.speed=self.speed+self.count
            else:
                self.gameOver = True
                cv2.putText(self.img,"Fin del juego",(int(self.cap.width()/4),int(self.cap.height()/2)),cv2.FONT_HERSHEY_COMPLEX,2,(17, 148, 222 ),5)

    def loop(self):
        while True:
            if self.gameOver is False:
                try:
                    self.img = self.cap.read()
                    cv2.putText(self.img,str(self.count),(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(86, 27, 241 ),5)
                    self.overlay()
                except: pass
                self.pos[1] += self.speed
                if self.pos[1]>(self.cap.height()-50): self.resetobject()
                self.mouthdetection()
                self.distance()
                self.objectDistance()
                self.isOpen()
                self.eat()
            cv2.imshow("Image",self.img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("r"):
                self.resetobject()
                self.gameOver = False
                self.count = 0
            elif key == ord("q"): break
        cv2.destroyAllWindows()
    
    def overlay(self):
        hf,wf,_ = self.currentObject.shape
        hb,wb,cb = self.img.shape
        *_,mask = cv2.split(self.currentObject)
        maskBGRA = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        imgRGBA = cv2.bitwise_and(self.currentObject, maskBGRA)
        imgRGB = cv2.cvtColor(imgRGBA, cv2.COLOR_BGRA2BGR)
        imgMaskFull = np.zeros((hb, wb, cb), np.uint8)
        imgMaskFull[self.pos[1]:hf + self.pos[1], self.pos[0]:wf + self.pos[0], :] = imgRGB
        imgMaskFull2 = np.ones((hb, wb, cb), np.uint8) * 255
        maskBGRInv = cv2.bitwise_not(maskBGR)
        imgMaskFull2[self.pos[1]:hf + self.pos[1], self.pos[0]:wf + self.pos[0], :] = maskBGRInv
        self.img = cv2.bitwise_and(self.img, imgMaskFull2)
        self.img = cv2.bitwise_or(self.img, imgMaskFull)

    def probgame(self,type: str = "fruits"):
        self.cap = Camera().start()
        self.initialize(type=type)
        self.loop()

if __name__ == "__main__":
    game = Game(dificult=0).probgame()