#!/usr/bin/python3
import sys





# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python opencv ( 範例 )"
# MyCodeString = '''
# ###  Python opencv 範例程式 ####
# ### file: mainCode_Python_opencv
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python opencv ( 範例 )"
# MyCodeString = '''
# ###  Python opencv 範例程式 ####
# ### file: mainCode_Python_opencv
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( Text 文件掃描-可調對比亮度 )"
MyCodeString = '''
###  Python opencv Text 文件掃描-可調對比亮度 ####
### file: mainCode_Python_opencv
import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


cap = cv2.VideoCapture(0)
cap.set(10,150)

###################################
widthImg  = 540
heightImg = 640
#####################################

windowName    = "dstImage"  # 視窗的名稱
cv2.namedWindow(windowName,1)

bright   = 255
contrast = 127

def empty(a): pass
cv2.createTrackbar( 'Bright'   , windowName, bright   , 2*255, empty ) #Brightness value range -255 to 255
cv2.createTrackbar( 'Contrast' , windowName, contrast , 2*127, empty ) #Contrast value range -127 to 127

while True:
    success, original = cap.read()
    # original = cv2.imread("paper.jpg")
    original = cv2.resize( original , (widthImg,heightImg))

    img = original.copy()

    bright   = cv2.getTrackbarPos( 'Bright'   , windowName )
    contrast = cv2.getTrackbarPos( 'Contrast' , windowName ) 

    #### 調整亮度 對比 ####################################################################
    bright   = int(( bright -  0 ) * ( 255 + 255 ) / ( 510 - 0 ) -255 )
    contrast = int(( contrast -0 ) * ( 127 + 127 ) / ( 254 - 0 ) -127 )
    if bright != 0:
        if bright > 0:
            shadow = bright
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + bright
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
 
        effect = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)
    else:
        effect = img.copy()
 
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f) 
        effect = cv2.addWeighted(effect, alpha_c, effect, 0, gamma_c) 
    #### END 調整亮度 對比 ####################################################################

    ### 第一次圖片處理 #######################################################
    imgGray  = cv2.cvtColor(effect,cv2.COLOR_BGR2GRAY)          ## 轉灰階 
    imgBlur  = cv2.GaussianBlur(imgGray,(5,5),1)                ## 高斯模糊
    imgCanny = cv2.Canny(imgBlur,200,200)                       ## 邊緣檢測
    imgDial  = cv2.dilate(imgCanny,np.ones((5,5)),iterations=2) ## 增強邊緣檢測
    imgThres = cv2.erode(imgDial  ,np.ones((5,5)),iterations=1) ## 減弱邊緣檢測
    ### END 第一次圖片處理 ##################################################

    imgContour = effect.copy()

    ### 第二次圖片處理 #######################################################
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(imgThres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) ## 找到邊角
    for cnt in contours:
        area = cv2.contourArea(cnt) ## 計算面積

        if area>5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) ## 畫出四邊
            peri = cv2.arcLength(cnt,True)                        ## 取得 邊緣長度
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)         ## 取得 頂點數量
            x,y,w,h = cv2.boundingRect(approx)                    ## 取得 頂點座標
            cv2.putText(imgContour, str(int(area)) , (x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) ## 畫出面積
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (0, 0, 255), 20)    ## 畫出四個角    
    ### end 第二次圖片處理 #######################################################

    ### 第三次圖片處理 #######################################################
    if biggest.size !=0:
        ################################
        myPoints = biggest.reshape((4,2))
        myPointsNew = np.zeros((4,1,2),np.int32)
        add = myPoints.sum(1)
        #print("add", add)
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] = myPoints[np.argmax(add)]
        diff = np.diff(myPoints,axis=1)
        myPointsNew[1]= myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        biggest = myPointsNew
        #print("NewPoints",myPointsNew)
        ################################
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        ################################
        imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
        imgWarped  = cv2.resize(imgCropped,(widthImg,heightImg))
    ### end 第三次圖片處理 #######################################################

    # img        = cv2.resize( img        , (widthImg,heightImg))
    # imgCanny   = cv2.resize( imgCanny   , (widthImg,heightImg))
    # imgThres   = cv2.resize( imgThres   , (widthImg,heightImg))
    # imgContour = cv2.resize( imgContour , (widthImg,heightImg))
    # imgWarped  = cv2.resize( imgWarped  , (widthImg,heightImg))

    try:
        cv2.imshow( windowName , stackImages( 0.6, ([img,imgCanny,imgThres,imgContour,imgWarped])     ) )
    except:
        cv2.imshow( windowName , stackImages( 0.6, ([img,imgCanny,imgThres,imgContour])     ) )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( Text 文件掃描 )"
MyCodeString = '''
###  Python opencv 範例程式 ####
### file: mainCode_Python_opencv
import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

###################################
widthImg  = 540
heightImg = 640
#####################################

cap = cv2.VideoCapture(0)
cap.set(10,150)

windowName    = "dstImage"  # 視窗的名稱
cv2.namedWindow(windowName,1)

while True:
    success, img = cap.read()
    # img = cv2.imread("paper.jpg")

    img = cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()

    ### 第一次圖片處理 #######################################################
    imgGray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)             ## 轉灰階 
    imgBlur  = cv2.GaussianBlur(imgGray,(5,5),1)                ## 高斯模糊
    imgCanny = cv2.Canny(imgBlur,200,200)                       ## 邊緣檢測
    imgDial  = cv2.dilate(imgCanny,np.ones((5,5)),iterations=2) ## 增強邊緣檢測
    imgThres = cv2.erode(imgDial  ,np.ones((5,5)),iterations=1) ## 減弱邊緣檢測
    ### END 第一次圖片處理 ##################################################

    ### 第二次圖片處理 #######################################################
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(imgThres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) ## 找到邊角
    for cnt in contours:
        area = cv2.contourArea(cnt) ## 計算面積

        if area>5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) ## 畫出四邊
            peri = cv2.arcLength(cnt,True)                        ## 取得 邊緣長度
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)         ## 取得 頂點數量
            x,y,w,h = cv2.boundingRect(approx)                    ## 取得 頂點座標
            cv2.putText(imgContour, str(int(area)) , (x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2) ## 畫出面積
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (0, 0, 255), 20)    ## 畫出四個角    
    ### end 第二次圖片處理 #######################################################

    ### 第三次圖片處理 #######################################################
    if biggest.size !=0:
        ################################
        myPoints = biggest.reshape((4,2))
        myPointsNew = np.zeros((4,1,2),np.int32)
        add = myPoints.sum(1)
        #print("add", add)
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] = myPoints[np.argmax(add)]
        diff = np.diff(myPoints,axis=1)
        myPointsNew[1]= myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
        biggest = myPointsNew
        #print("NewPoints",myPointsNew)
        ################################
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        ################################
        imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
        imgWarped  = cv2.resize(imgCropped,(widthImg,heightImg))
    ### end 第三次圖片處理 #######################################################

    cv2.imshow( windowName , stackImages( 0.6, ([img,imgCanny,imgThres,imgContour,imgWarped])     ) )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( OCR 文字辨識 )"
MyCodeString = '''
###  Python opencv OCR 文字辨識 ####
### file: mainCode_Python_opencv
import cv2
import pytesseract
import numpy as np
from PIL import Image, ImageDraw, ImageFont , ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'tesseract'

## cv2 顯示中文
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype( "NotoSansCJK-Bold.ttc", textSize, encoding="utf-8")

    draw.text((left, top), text, textColor, font=fontText)

    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

### 偵測文字 ##########################################
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_data(img,lang='chi_tra') ## 檢測中文

for line in boxes.splitlines():
    if line[0] == "5":
        print(line)
        b = line.split("\t")
        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9]) 

        myWord = b[11]
        cv2.rectangle(img, (x,y), (w+x,h+y), (50, 50, 255), 2)
        # cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
        print(myWord)
        img = cv2ImgAddText(img, myWord , x, y-30, (255, 0, 0), 20)

cv2.imshow('img', img)
cv2.waitKey(0)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 邊緣檢測-強化去雜訊 )"
MyCodeString = '''
###  Python opencv 邊緣檢測-強化去雜訊 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    morph = img.copy()

    # 通過擴大的內核交替關閉和打開來使圖像平滑
    # OpenCV中的形態學轉換操作有七種：腐蝕，膨脹，開運算，閉運算，形態學梯度，禮帽，黑帽。

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))  # 返回指定形狀和尺寸的結構元素 , MORPH_RECT(矩形) / MORPH_CROSS (交叉形) / MORPH_ELLIPSE (橢圓形)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)    # (閉運算)先膨脹，後腐蝕，去黑噪點 	先開再合，淺色成分得勢
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)     # (開運算)先腐蝕，後膨脹，去白噪點 	先合再開，對淺色成分不利

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))  # 返回指定形狀和尺寸的結構元素 , MORPH_RECT(矩形) / MORPH_CROSS (交叉形) / MORPH_ELLIPSE (橢圓形)
    gradient_image = cv2.morphologyEx(morph, cv2.MORPH_GRADIENT, kernel) #(形態學梯度) 一幅影象腐蝕與膨脹的區別，可以得到輪廓 	數值上解釋為：膨脹減去腐蝕

    # 將梯度圖像分成通道
    image_channels = np.split(np.asarray(gradient_image), 3, axis=2)
    channel_height, channel_width, _ = image_channels[0].shape

    # 將 Otsu閾值 套用 於每個 channel
    for i in range(0, 3):
        _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        image_channels[i]    = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))

    disImage = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2) # 合併 channels

    cv2.imshow("Original",  stackImages(0.7, ( [img,disImage] )) )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 邊緣檢測強化版-可調亮度對比 )"
MyCodeString = '''
###  Python opencv 邊緣檢測強化版-可調亮度對比 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

def empty(a): pass

cap = cv2.VideoCapture(0)
windowName    = "dstImage"  # 視窗的名稱

cv2.namedWindow(windowName,1)
bright   = 255
contrast = 127

cv2.createTrackbar( 'Bright'   , windowName, bright   , 2*255, empty ) #Brightness value range -255 to 255
cv2.createTrackbar( 'Contrast' , windowName, contrast , 2*127, empty ) #Contrast value range -127 to 127

while True:

    sucess, original = cap.read()
    img = original.copy()    

    bright   = cv2.getTrackbarPos( 'Bright'   , windowName )
    contrast = cv2.getTrackbarPos( 'Contrast' , windowName ) 

    #### 調整亮度 對比 ####################################################################
    bright   = int(( bright -  0 ) * ( 255 + 255 ) / ( 510 - 0 ) -255 )
    contrast = int(( contrast -0 ) * ( 127 + 127 ) / ( 254 - 0 ) -127 )
    if bright != 0:
        if bright > 0:
            shadow = bright
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + bright
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
 
        effect = cv2.addWeighted(img, alpha_b, img, 0, gamma_b)
    else:
        effect = img.copy()
 
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f) 
        effect = cv2.addWeighted(effect, alpha_c, effect, 0, gamma_c) 
    #### END 調整亮度 對比 ####################################################################

    orgCanny  = cv2.Canny(  original ,150,200)                                  ## 一般邊緣檢測
    orgCanny2 = cv2.dilate( orgCanny , np.ones((5,5),np.uint8) , iterations=1 ) ## 一般邊緣檢測-增強

    imgCanny  = cv2.Canny( effect ,150,200)                                     ## 調整亮度對比-邊緣檢測
    imgCanny2 = cv2.dilate( imgCanny , np.ones((5,5),np.uint8) , iterations=1 ) ## 調整亮度對比-邊緣檢測-增強

    cv2.imshow( windowName , stackImages( 0.7,(  [ original , orgCanny , orgCanny2 ],
                                                 [ effect   , imgCanny , imgCanny2 ]   )))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 邊緣檢測-標示面積 )"
MyCodeString = '''
###  Python opencv 邊緣檢測-標示面積 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50) #亮度

while True:
    sucess, img = cap.read()

    imgGray  = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )
    imgBlur  = cv2.GaussianBlur( imgGray , (7,7),1  )
    imgCanny = cv2.Canny( imgBlur,50,50)
    imgCanny = cv2.dilate( imgCanny , np.ones((5,5),np.uint8) , iterations=2 ) ## 邊緣檢測-增強

    imgContour = img.copy()
    contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) ## 找尋邊角    

    time.sleep(0.2)

    for cnt in contours:
        area    = cv2.contourArea(cnt)                 ## 取得 面積        
        peri    = cv2.arcLength(cnt,True)              ## 取得 邊緣長度
        approx  = cv2.approxPolyDP(cnt,0.02*peri,True) ## 取得 頂點數量
        x,y,w,h = cv2.boundingRect(approx)             ## 取得 頂點座標
        # print(x,y,area,type(area))

        ## 面積大於 200 顯示文字
        if area > 200:
            try:
                cv2.drawContours( imgContour , cnt , -1 ,(255,0,0) ,3  ) ## 畫出外框
                cv2.putText(imgContour, str(int(area))   , (x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),1) ## 標注
            except:
                pass

    cv2.imshow("Original",  stackImages(0.7, ( [img,imgCanny,imgContour] )) )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( HSV mask 去背 )"
MyCodeString = '''
###  Python opencv HSV mask 去背 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

# https://youtu.be/WQeoO7MI0Bs?t=3377

def empty(a):    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar( "Hue Min","TrackBars" ,   0 , 179 , empty )
cv2.createTrackbar( "Hue Max","TrackBars" ,  19 , 179 , empty )
cv2.createTrackbar( "Sat Min","TrackBars" , 110 , 255 , empty )
cv2.createTrackbar( "Sat Max","TrackBars" , 240 , 255 , empty )
cv2.createTrackbar( "Val Min","TrackBars" , 153 , 255 , empty )
cv2.createTrackbar( "Val Max","TrackBars" , 255 , 255 , empty )

while True:
    img = cv2.imread("test2.png")
    imgHSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos( "Hue Min","TrackBars" )
    h_max = cv2.getTrackbarPos( "Hue Max","TrackBars" )
    s_min = cv2.getTrackbarPos( "Sat Min","TrackBars" )
    s_max = cv2.getTrackbarPos( "Sat Max","TrackBars" )
    v_min = cv2.getTrackbarPos( "Val Min","TrackBars" )
    v_max = cv2.getTrackbarPos( "Val Max","TrackBars" )

    # print(h_min,h_max,s_min,s_max,v_min,v_max    )

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("img",stackImages(0.7,([img,imgHSV,mask,imgResult])))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 擷取 撲克牌-區塊 轉正 )"
MyCodeString = '''
###  Python opencv 撲克牌-區塊 轉正 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

## 擷取圖片 轉成正面 
# https://raw.githubusercontent.com/murtazahassan/Learn-OpenCV-in-3-hours/master/Resources/cards.jpg  ## 撲克牌.jpg

img = cv2.imread("cards.jpg")

width , height = 200,200 ## 定義輸出後的大小
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])     # 定義 擷取的座標點
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])   # 定義 輸出後的座標點
matrix = cv2.getPerspectiveTransform(pts1, pts2)        # 計算轉換後的矩陣
img2 = cv2.warpPerspective(img,matrix,(width, height))  # 使用透視變換 進行轉換

cv2.imshow("output1",img)
cv2.imshow("output2",img2)

cv2.waitKey(0)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 基本-劃線 寫字 劃圈 )"
MyCodeString = '''
###  Python opencv 基本-劃線 寫字 劃圈 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

img = np.zeros( (512,512,3) , dtype=np.uint8  )
img[:]             = 255,0,0   ## 整張變成藍色
img[10:200,50:200] = 255,0,0   ## [y1:y2,x1:x2] ## 區域變成藍色
cv2.line(      img , (0,0),(100,300),(0,255,0),5 )  ## 劃直線
cv2.rectangle( img , (0,0),(100,300),(0,0,255),5 )  ## 劃長方形
cv2.rectangle( img , (0,0),(100,300),(0,0,255),cv2.FILLED )  ## 劃 長方形+填滿
cv2.circle( img , (200,300),100, (255,255,0),2 )  ## 劃 圓圈

cv2.putText( img , "okok" , (200,100) , cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),1  )  ## 圖片寫字
cv2.imshow("output1",img)
cv2.waitKey(0)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 濾鏡-灰階,高斯模糊,邊緣檢測 )"
MyCodeString = '''
###  Python opencv 濾鏡-灰階,高斯模糊,邊緣檢測 增強 減弱 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,50) #亮度

while True:
    sucess, img = cap.read()
    # img = cv2.imread("test.jpg")

    imgResiz     = cv2.resize( img , (300,200) )          ## 變更大小 
    imgCropped   = img[0:150,0:600]                       ## 剪裁圖片 img[height:width]
    imgGray      = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  ## 轉灰階
    imgBlur      = cv2.GaussianBlur(imgGray, (17,17),0 )  ## 高斯模糊

    imgCanny     = cv2.Canny(img,150,200)                                              ## 邊緣檢測
    imgDialation = cv2.dilate( imgCanny     , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-增強
    imgEroded    = cv2.erode(  imgDialation , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-減弱

    # cv2.imshow( "imgGray"      , imgGray      ) ## 轉灰階
    # cv2.imshow( "imgBlur"      , imgBlur      ) ## 高斯模糊
    # cv2.imshow( "imgCanny"     , imgCanny     ) ## 邊緣檢測
    # cv2.imshow( "imgDialation" , imgDialation ) ## 邊緣檢測-增強
    # cv2.imshow( "imgEroded"    , imgEroded    ) ## 邊緣檢測-減弱

    cv2.imshow( "IMG" , stackImages(0.5,[[img,imgGray,imgBlur],[imgCanny,imgDialation,imgEroded]]) )

    if cv2.waitKey(1) & 0xFF == ord('q'):        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 邊緣檢測 )"
MyCodeString = '''
###  Python opencv 邊緣檢測 ####
### file: mainCode_Python_opencv
import cv2,time
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,50) #亮度

while True:
    sucess, img = cap.read()
    # img = cv2.imread("test.jpg")

    img1 = cv2.Canny( img,150,200)                                     ## 邊緣檢測
    img2 = cv2.dilate( img1 , np.ones((5,5),np.uint8) , iterations=1 ) ## 邊緣檢測-增強

    cv2.imshow( "CAM Test" , stackImages(0.7,[img,img1,img2]) )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 人臉辨識 Video)"
MyCodeString = '''
###  Python opencv cv2 人臉辨識 Video ####
### file: mainCode_Python_opencv
import numpy as np
import cv2

## 參數0是鏡頭
## cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video2.mp4')
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

## 連續讀取每一個 frame
while cap.isOpened():
    
    ## 讀取一個 frame
    flag,frame = cap.read()
    
    ## 讀取最後一個 frame 後，結束
    if flag == False:
        break
    
    ## 人臉識別，畫圈圈
    gray = cv2.cvtColor(frame,code = cv2.COLOR_BGR2GRAY)
    face_zone = detector.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5)
    for x,y,w,h in face_zone:
        cv2.circle(frame,center = (x + w//2,y + h//2),radius = w//2,color = [0,0,255],thickness = 2)
    
    ## 顯示 frame
    cv2.imshow('test',frame)
    
    if ord('q') == cv2.waitKey(20):
        break
        
cv2.destroyAllWindows()
cap.release();
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 人臉辨識 )"
MyCodeString = '''
###  Python opencv cv2 人臉辨識 ####
### file: mainCode_Python_opencv

import numpy as np
import cv2

myImg = cv2.imread('star.jpg')

## 重新轉換圖片大小
# myImg2 = cv2.resize(myImg,dsize = (1200,800))

# 轉成黑白，尺寸維持
gray = cv2.cvtColor(myImg,code = cv2.COLOR_BGR2GRAY)

## 使用人臉數據 xml ，Google haarcascade_frontalface_default.xml
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# ScaleFactor：每次搜尋方塊減少的比例
# minNeighbers：每個目標至少檢測到幾次以上，才可被認定是真數據。
# minSize：設定數據搜尋的最小尺寸 ，如 minSize=(40,40)
# maxSize：設定數據搜尋的最大尺寸 ，如 maxSize=(150,150)

face_zone = detector.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7 ,minSize = (50,50),maxSize = (150,150))

# 偵測人臉，畫框框
for x,y,w,h in face_zone:    
    ## 方框框
    #cv2.rectangle(myImg,pt1 = (x,y),pt2 = (x + w,y + h),color = [0,255,0],thickness = 2)
    
    ## 圓框框
    #cv2.circle(myImg,center = (x + w//2,y + h//2),radius = w//2, color = color.tolist(), thickness = 2)

cv2.imshow('myImg',myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( cv2 圖片操作 )"
MyCodeString = '''
###  Python opencv  cv2 圖片操作 ####
### file: mainCode_Python_opencv

import numpy as np
import cv2

### 顯示陣列的大小
myImg.shape

### 顯示圖檔
cv2.imshow('myImg',myImg)
# 等待鍵盤輸入，0毫秒，無限等待
cv2.waitKey(0)
cv2.destroyAllWindows()

### 轉成灰階
# cv2 讀取圖片，顏色通道是 BGR 藍綠紅
# PIL 2讀取圖片，顏色通道是 RGB

myImg2 = cv2.cvtColor(myImg,code = cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',myImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()

### 寫入圖片
cv2.imwrite('star2.jpg',myImg2)

### 顯示陣列的大小
myImg2.shape

### 重新 resize 圖片
myImg3 = cv2.resize(myImg,dsize = (440,666))
myImg3.shape

### 顯示圖檔
cv2.imshow('gray',myImg3)
while True:
    if ord('q') == cv2.waitKey(1000):
        break
cv2.destroyAllWindows()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python opencv ( 副程式-堆疊顯示圖片 )"
MyCodeString = '''
###  Python opencv 副程式-堆疊顯示圖片 ####
### file: mainCode_Python_opencv
def stackImages(scale,imgArray):
    ## this code from https://github.com/murtazahassan
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")









