import os
import cv2


class ObjectsImport:
    def __init__(self):
        self.fileDirectory = os.path.dirname(os.path.abspath(__file__))

    def importobjects(self,type: str = "noneatable"):
        if type == "fruits" or type == "vegetables":
            folderEatable = f'{self.fileDirectory}\\Objects\\eatable\\{type}'
        else:folderEatable = f'{self.fileDirectory}\\Objects\\{type}'
        objects = os.listdir(folderEatable)
        objectsbin = []
        for object in objects:
            objectsbin.append(cv2.imread(f'{folderEatable}/{object}', cv2.IMREAD_UNCHANGED))
        return objectsbin