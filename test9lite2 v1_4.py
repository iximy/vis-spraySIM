
import cv2 
import numpy as np 
import pygame
pygame.init()
song = pygame.mixer.Sound('aero2.mp3')



pts = np.array([[47,45],[72,22],[265,22],[292,45],[292,145],[250,145],[225,120],[112,120],[80,145],[47,145],[47,45]], np.int32)
pts = pts.reshape((-1,1,2))

# калбэк функции мыши
drawing = False

def draw_circle(event,x,y,flags,param): 
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        song.play()
    if event == cv2.EVENT_RBUTTONDOWN:

        gray = cv2.cvtColor(cv2.blur(img,(52,52)),cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
        color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
        cv2.polylines(color,[pts],True,(0,255,255),5)
        resizedcolor = cv2.resize(color,None,fx=4, fy=4)
        cv2.imshow('image',resizedcolor)
        
    elif(event == cv2.EVENT_MOUSEMOVE): 
        if drawing == True:
            # cv2.circle(img,(x,y),100,(255,255, 0),-1) 
            cv2.ellipse(img,(x//4,y//4),(12, 20), 0, 0, 360,(0,255,0), -1) 
            cv2.polylines(imgs,[pts],True,(0,255,255),2)
            resized = cv2.resize(cv2.addWeighted( cv2.blur(img,(12,12)), 0.5, imgs, 0.5, 0.0),None,fx=4, fy=4)
            cv2.imshow('image',resized)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        song.stop()
# создаем окно с размерами
img = np.zeros((180,320,3), np.uint8) 
imgs = np.zeros((180,320,3), np.uint8) 


cv2.namedWindow('image') 
cv2.setMouseCallback('image',draw_circle) 
cv2.polylines(imgs,[pts],True,(0,255,255),2)
resizedimgs = cv2.resize(imgs,None,fx=4, fy=4)
cv2.imshow('image', resizedimgs)

while(1): 




    if cv2.waitKey(20) & 0xFF == 27: 
        break 
cv2.destroyAllWindows() 
