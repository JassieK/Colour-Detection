import cv2
import pandas as pd


img_path = r'D:\Data Analytics\Colour Detection\picture.jpg'

#reading Image and resizing
img = cv2.imread(img_path)
img = cv2.resize(img, (700, 600))

#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file and giving name to each column
colorcsv = r'D:\Data Analytics\Colour Detection\colors.csv'
index = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv(colorcsv, names = index, header = None)


#function to calculate minimum distance to get color name
def get_Color_Name(B,G,R):
    minimum = 10000
    for i in range (len(csv)):
        d = abs(R - int(csv.loc[i , "R"])) +abs(G - int(csv.loc[i , "G"]))+abs(G - int(csv.loc[i , "G"]))
        if (d<=minimum):
            minimum = d
            cname = csv.loc[i , "color_name"]
    return cname
            

#Creating the draw function to get pixel value on click
def draw_function (event , x , y , flags , param):
   if event == cv2.EVENT_LBUTTONDBLCLK:
    global  r, g, b, xpos , ypos , clicked
    clicked = True 
    xpos = x
    ypos = y
    b , g, r = img [y,x]
    b = int(b)
    g =int(g)
    r = int(r)
    
    
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while (1):
    cv2.imshow("image",img)
    if(clicked):
     cv2.rectangle(img, (20,20), (720,60), (b,g,r), -1)
     text = get_Color_Name(b, g, r) + ' R =' + str(r) + ' G =' + str(g) +' B =' + str(b)
     cv2.putText(img,text,(50,50),2,0.8, (255,255,255), 2, cv2.LINE_AA)
     if (r+g+b)>=600:
      cv2.putText(img,text,(50,50),2,0.8, (0,0,0), 2, cv2.LINE_AA)
     clicked = False
        
    #if user clicks escape
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()