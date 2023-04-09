import cv2
import mediapipe as mp
import math

class Face:
    def __init__(self):
        self.mpFace = mp.solutions.face_mesh
        self.face = self.mpFace.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def findFace(self, img):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face.process(self.imgRGB)
        face = []
        if self.results.multi_face_landmarks:
            for faceLandmark in self.results.multi_face_landmarks:
                for _,lm in enumerate(faceLandmark.landmark):
                    ih,iw,_ = img.shape
                    x,y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
        return face

    def findDistance(self,p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        x, y = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        return length