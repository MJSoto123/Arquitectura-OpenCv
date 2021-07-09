import cv2
import numpy as np
import imutils
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('Prueba_2.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = imutils.resize(frame, width=720)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Dibujamos un rectángulo en frame, para señalar el estado
    # del área en análisis (movimiento detectado o no detectado)
    cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
    color = (0, 255, 0)
    texto_estado_A = "A ---"
    # Especificamos los puntos extremos del área a analizar
    area_A = np.array([[0,40], [360,40], [360,290], [0,290]])
    
    # Con ayuda de una imagen auxiliar, determinamos el área
    # sobre la cual actuará el detector de movimiento
    imAux_A = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux_A = cv2.drawContours(imAux_A, [area_A], -1, (255), -1)
    image_area_A = cv2.bitwise_and(gray, gray, mask=imAux_A)
    # Obtendremos la imagen binaria donde la región en blanco representa
    # la existencia de movimiento
    fgmask_A = fgbg.apply(image_area_A)
    fgmask_A = cv2.morphologyEx(fgmask_A, cv2.MORPH_OPEN, kernel)
    fgmask_A = cv2.dilate(fgmask_A, None, iterations=2)
    # Encontramos los contornos presentes en fgmask_A, para luego basándonos
    # en su área poder determina si existe movimiento
    cnts = cv2.findContours(fgmask_A, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mov_A = 0
    for cnt in cnts:
        if cv2.contourArea(cnt) > 2000:
            # x, y, w, h = cv2.boundingRect(cnt)
            # cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
            texto_estado_A = "A ooo"
            color = (0, 0, 255) 
    # Visuzalizamos el alrededor del área que vamos a analizar
    # y el estado de la detección de movimiento        
    cv2.drawContours(frame, [area_A], -1, color, 2)
    cv2.putText(frame, texto_estado_A , (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)


# AREA B  
    color_B = (0, 255, 0)
    texto_estado_B = "B ---"
    area_B  = np.array([[360,40], [720,40], [720,290], [360,290]])

    imAux_B = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux_B = cv2.drawContours(imAux_B, [area_B], -1, (255), -1)
    image_area_B = cv2.bitwise_and(gray, gray, mask=imAux_B)

    fgmask_B = fgbg.apply(image_area_B)
    fgmask_B = cv2.morphologyEx(fgmask_B, cv2.MORPH_OPEN, kernel)
    fgmask_B = cv2.dilate(fgmask_B, None, iterations=2)

    cnts_B = cv2.findContours(fgmask_B, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in cnts_B:
        if cv2.contourArea(cnt) > 2000:
            texto_estado_B = "B ooo"
            color_B = (0, 0, 255)
    
    cv2.drawContours(frame, [area_B], -1, color_B, 2)
    cv2.putText(frame, texto_estado_B , (120, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color_B,2)

# AREA C  
    color_C = (255, 0, 0)
    texto_estado_C = "C ---"
    area_C  = np.array([[0,290], [360,290], [360,540], [0,540]])

    imAux_C = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux_C = cv2.drawContours(imAux_C, [area_C], -1, (255), -1)
    image_area_C = cv2.bitwise_and(gray, gray, mask=imAux_C)

    fgmask_C = fgbg.apply(image_area_C)
    fgmask_C = cv2.morphologyEx(fgmask_C, cv2.MORPH_OPEN, kernel)
    fgmask_C = cv2.dilate(fgmask_C, None, iterations=2)

    cnts_C = cv2.findContours(fgmask_C, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in cnts_C:
        if cv2.contourArea(cnt) > 2000:
            texto_estado_C = "C ooo"
            color_C = (0, 0, 255)
    
    cv2.drawContours(frame, [area_C], -1, color_C, 2)
    cv2.putText(frame, texto_estado_C , (230, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color_C,2)

# AREA D
    color_D = (255, 0, 0)
    texto_estado_D = "D ---"
    area_D  = np.array([[360,290], [720,290], [720,540], [360,540]])

    imAux_D = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux_D = cv2.drawContours(imAux_D, [area_D], -1, (255), -1)
    image_area_D = cv2.bitwise_and(gray, gray, mask=imAux_D)

    fgmask_D = fgbg.apply(image_area_D)
    fgmask_D = cv2.morphologyEx(fgmask_D, cv2.MORPH_OPEN, kernel)
    fgmask_D = cv2.dilate(fgmask_D, None, iterations=2)

    cnts_D = cv2.findContours(fgmask_D, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    cont_D = 0;
    for cnt in cnts_D:
        if cv2.contourArea(cnt) > 2000:
            texto_estado_D = "D ooo"
            color_D = (0, 0, 255)
            
    cv2.drawContours(frame, [area_D], -1, color_D, 2)
    cv2.putText(frame, texto_estado_D , (340, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color_D,2)

# SHOW FRAME
    cv2.imshow("frame", frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
