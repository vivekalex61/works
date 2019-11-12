# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:17:51 2019

@author: vivekz
"""

import cv2
import numpy as np
import time
import serial
#import camerav.py
path="C:\\Users\\vivekz\\Desktop\\ip\\caliberate.jpg" 
oimg=cv2.imread(path,1)  
windowname="window"
#so=serial.Serial(port="COM4",baudrate=9600,timeout=2,stopbits=serial.STOPBITS_ONE)
right_clicks=list()
img=cv2.resize(oimg,(1024,512))
cmtopixelx=100/1024
cmtopixely=50/512.0
x=4
cm=100/20
r=cm*x
p=int(r)
#cv2.imshow('oho',camerav.cameracheck())

cv2.namedWindow(windowname)
#class mouse():
    
    

def circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),p,(0,255,0),1)
        
        
       # print(x,y)
        x1=x*cmtopixelx
        y1=y*cmtopixely
        xl=int(x1)
        yl=int(y1)
        
        right_clicks.append([xl,yl])
        print(xl,yl)
        
cv2.setMouseCallback(windowname,circle)       

def main():
    while(True):
        cv2.imshow(windowname,img)
        if cv2.waitKey(20)==27:
            print(right_clicks)
            for crd in right_clicks:
                xo=str(crd[0])
                yo=str(crd[1])
                print(xo,yo)     
                
                command="G41 "+"x"+str(0)+xo + " y"+str(0)+yo
                print(command)
                time.sleep(3)
                
     
                #write=so.write(command.encode())
                #time.sleep(22)
               
            break

    cv2.destroyAllWindows()    
    
    
    


    
    
     
if __name__=="__main__":
    
    
    main()
    
  
