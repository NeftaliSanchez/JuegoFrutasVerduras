import cv2

####
# imput the ID camera
####

def screenVideo():
    # PC - 0
    # Laptop - 2
    # if you have troveled shotting your camera, then
    # you'd need to change the number at cv2.VideoCapture(X)

    cap = cv2.VideoCapture(0)
    return cap

def main():
    screenVideo

if __name__ == '__main__':
    main()
