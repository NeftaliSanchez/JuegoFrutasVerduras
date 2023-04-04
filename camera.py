import cv2
from threading import Thread
from cvzone.FaceMeshModule import FaceMeshDetector as Fd


class Camera:
    def __init__(self):
        self.cap = None
        self.lastFrame = None
        self.stopped = False
        self.detector = Fd(maxFaces = 2)
    
    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self
    
    def update(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        while True:
            if self.stopped:
                return
            (result,image) = self.cap.read()
            if not result:
                self.stop()
                return 
            self.lastFrame = image
            

    def stop(self):
        self.stopped = True

    def read(self):
        return self.lastFrame

    def width(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    def height(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)