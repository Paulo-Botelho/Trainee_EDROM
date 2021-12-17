import cv2
import numpy as np



def main():
    def getpass():
        pass

    raw_input = input 
    alpha = 0.7
    beta = (1.0 - alpha)

    def empty(a):
        pass


    def stackImages(scale, imgArray):
        rows = len(imgArray)
        cols = len(imgArray[0])
        rowsAvailable = isinstance(imgArray[0], list)
        width = imgArray[0][0].shape[1]
        height = imgArray[0][0].shape[0]
        if rowsAvailable:
            for x in range(0, rows):
                for y in range(0, cols):
                    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                    else:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                    None, scale, scale)
                    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imageBlank = np.zeros((height, width, 3), np.uint8)
            hor = [imageBlank] * rows
            hor_con = [imageBlank] * rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
            ver = np.vstack(hor)
        else:
            for x in range(0, rows):
                if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                else:
                    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
                if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor = np.hstack(imgArray)
            ver = hor
        return ver


    ################################################################################

    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", 63, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 123, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 125, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 251, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 63, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

    frameWidth = 640
    frameHeight = 480

    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    ksize = (50, 50)

    while True:


        success, img = cap.read()

        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        #print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        
        
        mask = cv2.blur(mask,ksize, cv2.BORDER_DEFAULT) # Blur

        

        indices = np.where(mask> [100]) # procurando coordenadas na mascara e colocando em indices
                
        x,y = np.mean(indices, axis=1)
        
        x,y= coordenadas(x,y)
        print("Mean with axis along row :", x,y)

        #################################################################

        imgResult[mask > 100] = (0,0,220)
        imgResult[mask <=100] = img[mask<=100]

        
        dst = cv2.addWeighted(imgResult, alpha, img, beta, 0.0)
        

        imgStack = stackImages(0.6, ([img, imgHSV], [mask,dst]))
        cv2.imshow("Stacked Images", imgStack)

    

        cv2.waitKey(1)
   




def coordenadas(x,y):

    x_sit = 0
    y_sit = 0
    
    if y <= 640 and y > 460:
        y_sit = "direita"
    elif y < 280 and y >= 0:
        y_sit = "esquerda"
    elif y >= 280 and y <=460:
        y_sit = "centro"
    
    if x <= 480 and x > 280:
        x_sit = "embaixo"
    elif x < 200 and x >= 0:
        x_sit = "encima"
    elif x >= 200 and x <= 280:
        x_sit = "centro"
    
    x = x_sit
    y = y_sit

    return x, y


if __name__ == "__main__":
    main()