import cv2
import pandas as pd

cap = cv2.VideoCapture(0)

clicked = False
r = g = b = xpos = ypos = 0

colorcsv = r'D:\Data Analytics\Colour Detection\colors.csv'
index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv(colorcsv, names = index, header = None)

def get_Color_Name(B,G,R):
    minimum = 10000
    for i in range (len(csv)):
        d = abs(R - int(csv.loc[i , "R"])) +abs(G - int(csv.loc[i , "G"]))+abs(G - int(csv.loc[i , "G"]))
        if (d<=minimum):
            minimum = d
            cname = csv.loc[i , "color_name"]
    return cname


def draw_function (event , x , y , flags , param):
   if event == cv2.EVENT_LBUTTONDOWN:
    global  r, g, b, xpos , ypos , clicked
    clicked = True 
    xpos = x
    ypos = y
    b , g, r = frame [y,x]
    b = int(b)
    g =int(g)
    r = int(r)
    

cv2.namedWindow("frame")
cv2.setMouseCallback("frame",draw_function)


while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame , (700,600) , fx = 0.5 , fy = 0.5)
    cv2.imshow("frame",frame)
    
    
    cv2.rectangle(frame, (20,20), (720,60), (b,g,r), -1)
    text = get_Color_Name(b, g, r) + ' R = ' + str(r) + ' G = ' + str(g) +' B = ' + str(b)
    cv2.putText(frame,text,(50,50),2,0.8, (255,255,255), 2, cv2.LINE_AA)
    if (r+g+b)>=600:
        cv2.putText(frame,text,(50,50),2,0.8, (0,0,0), 2, cv2.LINE_AA)
        
        
    cv2.imshow("frame",frame)     
    clicked = False

    key = cv2.waitKey(1)
    if key == 27:
        break
   
cap.release()
cv2.destroyAllWindows()
    