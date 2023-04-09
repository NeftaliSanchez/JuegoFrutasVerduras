import cv2
from threading import Thread
from detection import Face as Facedetector


class Camera:
    def __init__(self):
        self.cap = None
        self.lastFrame = None
        self.stopped = False
        self.detector = Facedetector()
        self.flip =  bool
    
    def start(self):
        self.flip = False
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self
    
    def update(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        while True:
            if self.stopped: return
            (result,image) = self.cap.read()
            if not result:
                self.stop()
                return 
            if self.flip is True: image = cv2.flip(image,1)
            self.lastFrame = image

    def stop(self):
        self.stopped = True

    def read(self):
        return self.lastFrame

    def width(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    def height(self):
        return self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def config(self):
        img = None
        while True:
            while img is None:
                img = self.read()
            img = self.read()
            cv2.imshow("Image",img)
            key = cv2.waitKey(1)
            if key == ord("q"): break
            if key == ord("f"): self.flip =  not self.flip
        cv2.destroyAllWindows()