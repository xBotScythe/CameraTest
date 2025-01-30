"""
Camera.py - camera testing thing
1/29
"""
from djitellopy import Tello
import threading, cv2

# instantiate Tello 
# tello = Tello()

def readFrame(frame):
    # print("hello")
    # img = frame.frame
    cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Camera", 800, 600)
    cv2.imshow("Camera", frame) #Display to window

def main():
    # tello.connect()
    # tello.streamon()
    # frame_read = tello.get_frame_read()
    img = cv2.imread("netflix.png")
    readFrame(img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()