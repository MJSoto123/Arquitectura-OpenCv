from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
import imutils
import time
import keyboard

def Sensor(mask,color, arr):
  contornos, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 200:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])
      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame,(x,y),7,(0,255,0),-1)
      cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)    
      if((x>80 and x<300) and(y>35 and y<160)):
        texto_estado_A ="A ooo"
        cv2.putText(frame, texto_estado_A , (10, 525),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)
        if(arr[0]):
            # keyboard.write("c")
            arr[0]=False;
      else:
          arr[0]=True
        
      if((x>380 and x<600) and(y>35 and y<160)):
        texto_estado_B ="B ooo"
        cv2.putText(frame, texto_estado_B , (140, 525),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)
        if(arr[1]):
            # keyboard.write("z")
            arr[1]=False;
      else:
          arr[1]=True
      
      if((x>230 and x<440) and(y>160 and y<300)):
        texto_estado_C ="C ooo"
        cv2.putText(frame, texto_estado_C , (270, 525),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)
        if(arr[2]):
            # keyboard.write("s")
            arr[2]=False;
      else:
          arr[2]=True
 
      if((x>40 and x<270) and(y>300 and y<450)):
        texto_estado_D ="D ooo"
        cv2.putText(frame, texto_estado_D , (400, 525),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)
        if(arr[3]):
            # keyboard.write("e")
            arr[3]=False;
      else:
          arr[3]=True
      
      if((x>400 and x<640) and(y>300 and y<450)):
        texto_estado_E ="E ooo"
        cv2.putText(frame, texto_estado_E , (530, 525),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)
        if(arr[4]):
            # keyboard.write("q")
            arr[4]=False;
      else:
          arr[4]=True
  return arr

def video_de_entrada():
    global cap
    global frame
    global font
    # btnEnd.configure(state="active")
    # radFondo1.configure(state="disabled")
    # radFondo2.configure(state="disabled")
    lblInfoVideoPath.configure(text="")
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("Videos/S2_4.MP4")
    azulBajo = np.array([50,100,20],np.uint8)
    azulAlto = np.array([60,255,255],np.uint8)
    color = (255, 0 , 0)

    area_A = np.array([[80,35], [300,35], [300,160], [80,160]])
    area_B = np.array([[380,35], [600,35], [600,160], [380,160]])
    area_C = np.array([[230,160], [440,160], [440,300], [230,300]])
    area_D = np.array([[40,300], [270,300], [270,450], [40,450]])
    area_E = np.array([[400,300], [640,300], [640,450], [400,450]])

    arr = [True, True, True, True, True]
    time.sleep(4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret,frame = cap.read()
        frame = imutils.resize(frame, width=720)
        cv2.rectangle(frame,(0,490),(frame.shape[1],540),(0,0,0),-1)
        texto_estado_A = "A ---"
        texto_estado_B = "B ---"
        texto_estado_C = "C ---"
        texto_estado_D = "D---"
        texto_estado_E = "E ---"
        cv2.drawContours(frame, [area_A], -1, color, 2)
        cv2.drawContours(frame, [area_B], -1, color, 2)
        cv2.drawContours(frame, [area_C], -1, color, 2)
        cv2.drawContours(frame, [area_D], -1, color, 2)
        cv2.drawContours(frame, [area_E], -1, color, 2) 
        if ret == True:
            frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
            arr = Sensor(maskAzul,(200,200,40),arr)
            # print(arr)
            cv2.imshow('maskAzul',maskAzul)
            cv2.imshow('frame',frame)
            if cv2.waitKey(22) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()


root = Tk()
lblTitle = Label(root, text="PUMP IT UP CONTOLLER", font="bold")
lblTitle.grid(column=0, row=0, columnspan=10)
btnStart = Button(root, text="Iniciar camara", state="active", command=video_de_entrada)
btnStart.grid(column=0, row=2)

lblInfoVideoPath = Label(root, text="", width=70)
lblInfoVideoPath.grid(column=0, row=1)
lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)
root.mainloop()