import cv2
from PIL import ImageGrab
import numpy as np
from numpy.core.arrayprint import array2string
from win32api import GetSystemMetrics
import time

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
capure_video=cv2.VideoWriter('video1.mp4' ,fourcc,20.0,(width,height))
while True:
    screen_img=ImageGrab.grab(bbox=(0,0,width,height))
    array_img=np.array(screen_img)
    color_img=cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)
    capure_video.write(color_img)
    cv2.imshow('Screen Recorder  ',color_img)
    if cv2.waitKey(1)==ord('q'):
        break