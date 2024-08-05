import numpy as np
import cv2
from copy import deepcopy
NOBC=60
class WebcamCapture:

    CapturePhase=0
    arr=[]
    backCapture=False
   
    def __init__(self):
        cv2.namedWindow("Trackbar")
        cv2.createTrackbar("low_h","Trackbar",0,179,self.fun)
        cv2.createTrackbar("low_s","Trackbar",0,255,self.fun)
        cv2.createTrackbar("low_v","Trackbar",0,255,self.fun)
        cv2.createTrackbar("high_h","Trackbar",0,179,self.fun)
        cv2.createTrackbar("high_s","Trackbar",0,255,self.fun)
        cv2.createTrackbar("high_v","Trackbar",0,255,self.fun)

    
        
        vid=cv2.VideoCapture(0)
        while True:
            ret,frame=vid.read()
           
            if not ret:
                print("ERROR: capturing frame")
                return
            elif self.backCapture and self.CapturePhase<NOBC:
                self.captureBackground(frame)
                self.CapturePhase+=1
            elif self.CapturePhase==NOBC and self.backCapture:
                self.backgroundImage=self.getImg()
                self.backCapture=False
            else:
                frame=self.magicFrame(frame)
               

            cv2.imshow("Magic Cam",frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'): 
                break
            elif key == ord('r'):
                self.CapturePhase=0
                self.arr.clear()
                self.backCapture=True
           
            


        vid.release()
        cv2.destroyAllWindows()
    
    def captureBackground(self,frame):
        self.arr.append(deepcopy(frame))
        cv2.putText(frame,"Capturing background please move out of frame", (5,50), cv2.FONT_HERSHEY_COMPLEX, 0.7, 130)


    def getImg(self):
        
        sumImg=np.zeros(self.arr[0].shape, dtype=np.float32)
        for f in self.arr:
            sumImg+=np.array(f, dtype=np.float32)
        return (sumImg/len(self.arr)).astype(np.uint8)
   
    
        
        

    def magicFrame(self,frame):
        if not (hasattr(self, 'backgroundImage')):
            return frame
        
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lh=cv2.getTrackbarPos("low_h","Trackbar")
        ls=cv2.getTrackbarPos("low_s","Trackbar")
        lv=cv2.getTrackbarPos("low_v","Trackbar")
        hh=cv2.getTrackbarPos("high_h","Trackbar")
        hs=cv2.getTrackbarPos("high_s","Trackbar")
        hv=cv2.getTrackbarPos("high_v","Trackbar")


        lowerval=np.array([lh,ls,lv])
        highval=np.array([hh,hs,hv])
        mask=cv2.inRange(hsv,lowerval,highval)
        maskinv=255-mask

        rslt1=cv2.bitwise_and(self.backgroundImage,self.backgroundImage,mask=mask)
        rslt2=cv2.bitwise_and(frame,frame,mask=maskinv)

        rslt=cv2.bitwise_or(rslt1,rslt2)    
        return rslt
    
    def fun(self,val):
        return
      

       


