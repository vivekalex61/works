# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:28:16 2019

@author: vivekz
"""

import cv2
import numpy as np
#import camerav
import serial
import time

pre ='a'
global xlocationm
global ylocationm
path="C:\\Users\\vivekz\\Desktop\\ip\\caliberate.jpg"
#so=serial.Serial(port="COM4",baudrate=9600,timeout=2,stopbits=serial.STOPBITS_ONE)
#image2=camerav.cameracheck()

def main():
    
    

       
    
    cmtopixelx=100/1024.0
    cmtopixely=50/512.0

    frame=cv2.imread(path,1)
    frame=cv2.resize(frame,(1024,512))
    #cv2.imshow('image2',frame)
    noise=cv2.fastNlMeansDenoisingColored(frame,None,10,10)
    blur=cv2.GaussianBlur(noise,(5,5),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lowgreen=np.array([30,20,20])
    uppergreen=np.array([90,255,255])
    mask=cv2.inRange(hsv,lowgreen,uppergreen)
    
    edged = cv2.Canny(mask, 100, 200)
    cany = cv2.dilate(edged, None, iterations=1)
   



    _,contours,_=cv2.findContours(cany,1,2)
    #epsilon=0.6*cv2.arcLength(cany,True)
    #approx=cv2.approxPolyDP(cany,epsilon,True)
 
    cv2.drawContours(blur,contours, -1, (255, 255, 255),1)
    for cnt in contours:
         
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        centre=(int(x),int(y))
        radius=int(radius)
        cv2.circle(blur,centre,radius,(0,255,0),2)
         
        area=cv2.contourArea(cnt)
       
          
   
        if area >= 100 and area <=500 :
        
            m=cv2.moments(cnt)
            cx=int(m['m10']/m['m00']) #centre of the contour
            cy=int(m['m01']/m['m00'])
            
            (x,y),radius=cv2.minEnclosingCircle(cnt)
            centre=(int(cx),int(cy))
            radius=int(radius)
            cv2.circle(blur,centre,radius,(0,0,255),2)
        
            xlocationc=cx*cmtopixelx
            ylocationc=cy*cmtopixely
           
            # print(cx,cy)
            #print(xlocationc,ylocationc) #location of the contour detected
            #print(xlocationm,ylocationm)
            # print(area)
           
            p=int(xlocationc)
            q=int(ylocationc)
            h=str(p)
            j=str(q)
            print(p,q)
        #n=int(p[0])
       # m=int(q[0])
       
        
            command="G41 "+"x"+str(0)+h + " y"+str(0)+j
            print(command)
          
            time.sleep(0)
     
     #       write=so.write(command.encode())
     #       time.sleep(17)
     #       command2="G52"
           
            #while True:
            #    print(so.readline())
                
              #  if pre == str(so.readline()):
              #       out = so.read()
              #       print(out)
                     
   
 #   command3="G21"
 #   write=so.write(command3.encode())
    cv2.imshow('t',blur)
   # cv2.imshow('te',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()         
            
               
                
       
        
        
    
    #so.close()    
if __name__=="__main__":
    main()