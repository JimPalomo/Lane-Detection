import cv2 as cv
import numpy as np

class LaneDetection():
    def __init__(self, img):
        self.img = img  # img directory 

    def info(self):
        print(self.img)

    def default_prewitt(self):
        img = cv.imread(self.img) #Read image
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        prewitt_vertical = np.array([[-1,0,-1],[-1,0,-1],[-1,0,-1]])
        prewitt_horizontal = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        
        prewitt_vertical = cv.filter2D(img, -1, prewitt_vertical)  # -1 depth will be the same as source img 
        prewitt_horizontal = cv.filter2D(img, -1, prewitt_horizontal)  # -1 depth will be the same as source img 

        cv.imshow("Prewitt - Vertical Mask", prewitt_vertical)
        cv.imshow("Prewitt - Horizontal Mask", prewitt_horizontal)

        self.__closeAll()

    def default_sobel(self):
        img = cv.imread(self.img) #Read image
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert color image into grey-scale image 

        sobel_vertical = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        sobel_horizontal = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        
        sobel_vertical = cv.filter2D(img, -1, sobel_vertical)  # -1 depth will be the same as source img 
        sobel_horizontal = cv.filter2D(img, -1, sobel_horizontal)  # -1 depth will be the same as source img 

        cv.imshow("Sobel - Vertical Mask", sobel_vertical)
        cv.imshow("Sobel - Horizontal Mask", sobel_horizontal)

        self.__closeAll()

    def default_canny(self):
        img = cv.imread(self.img) # read image
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert color image into grey-scale image 

        canny_vertical = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        canny_horizontal = np.array([[-1,-1,-1],[0, 0, 0],[1,1,1]])
        
        canny_vertical = cv.filter2D(img, -1, canny_vertical)  # -1 depth will be the same as source img 
        canny_horizontal = cv.filter2D(img, -1, canny_horizontal)  # -1 depth will be the same as source img 

        cv.imshow("Canny - Vertical Mask", canny_vertical)
        cv.imshow("Canny - Horizontal Mask", canny_horizontal)

        self.__closeAll()

    def default_laplacian(self):
        img = cv.imread(self.img).astype('uint8')
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        laplacian_mask1 = np.array([[0,-1, 0],[-1,4,-1],[0,-1, 0]])
        laplacian_mask2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        
        laplacian_1 = cv.filter2D(img, -1, laplacian_mask1)  # -1 depth will be the same as source img 
        laplacian_2 = cv.filter2D(img, -1, laplacian_mask2)  # -1 depth will be the same as source img 

        cv.imshow("Laplacian - Mask 1", laplacian_1)
        cv.imshow("Laplacian - Mask 2", laplacian_2)

        self.__closeAll()
    
    def builtin_prewitt(self):
        imgOriginal = cv.imread(self.img)
        img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)       # convert color image into grey-scale image 
        cv.imshow("Original", imgOriginal)
        img = cv.blur(img, (5,5))                       # blurring image reduces noise
        img = cv.GaussianBlur(img,(5,5),0)              # Laplacian of Gaussian, LoG
        img = cv.GaussianBlur(img,(5,5),0)              # Laplacian of Gaussian, LoG
        
        prewitt_vertical = np.array([[-1,0,-1],[-1,0,-1],[-1,0,-1]])
        prewitt_horizontal = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
                
        prewitt_vertical = cv.filter2D(img, -1, prewitt_vertical)  # -1 depth will be the same as source img 
        prewitt_horizontal = cv.filter2D(img, -1, prewitt_horizontal)  # -1 depth will be the same as source img 

        cv.imshow("Prewitt", prewitt_vertical)    # black screen
        cv.imshow("Prewitt", prewitt_horizontal)

        self.__closeAll()

    def builtin_laplacian(self):
        imgOriginal = cv.imread(self.img)
        img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)       # convert color image into grey-scale image 
        cv.imshow("Original", imgOriginal)
        img = cv.GaussianBlur(img,(5,5),0)              # Laplacian of Gaussian, LoG
        img = cv.GaussianBlur(img,(5,5),0)              # Laplacian of Gaussian, LoG

        imgLaplacian = cv.Laplacian(img, ddepth=cv.CV_16S)
        imgLaplacian = cv.Laplacian(img, -1)
        cv.imshow("Laplacian", imgLaplacian)

        self.__closeAll()

    def builtin_sobel(self):
        imgOriginal = cv.imread(self.img)
        img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)       # convert color image into grey-scale image 
        cv.imshow("Original", imgOriginal)
        img = cv.GaussianBlur(img,(5,5),0)              # Sobel of Gaussian, SoG
        img = cv.GaussianBlur(img,(5,5),0)              # Sobel of Gaussian, SoG

        imgSobel = cv.Sobel(img, ddepth=cv.CV_16U, dx=1, dy=0)
        cv.imshow("Sobel Original", imgSobel)   # black screen

        self.__closeAll()

    def builtin_canny(self):
        imgOriginal = cv.imread(self.img)
        img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)       # convert color image into grey-scale image 
        cv.imshow("Original", imgOriginal)
        img = cv.GaussianBlur(img,(5,5),0)                      # Sobel of Gaussian, SoG
        img = cv.GaussianBlur(img,(5,5),0)                      # Sobel of Gaussian, SoG

        imgCanny = cv.Canny(img, 150, 200)  # Canny(img, high threshold, low threshold, apertureSize for Sobel smooth/sharpen, L2gradient)  
        cv.imshow("Canny Original", imgCanny)

        # L2gradient (gradient magnitude)
        newImg = cv.Canny(img, 150, 200, L2gradient=5)       # decrease in background edges
        # newImg = cv.Canny(img, 150, 200, L2gradient=50)      # decrease in bg edges
        # newImg = cv.Canny(img, 150, 200, L2gradient=500)     # decrease in bg edges

        # apertureSize (smoothing/sharpening)
        # newImg = cv.Canny(img, 150, 200, apertureSize=3)     # no change
        # newImg = cv.Canny(img, 150, 200, apertureSize=5)     # edge overloaded (too many)
        # newImg = cv.Canny(img, 150, 200, apertureSize=7)     # edge overloaded (too many x2)

        cv.imshow("Updated Canny w/ Parameters", newImg)        
        self.__closeAll()

    def builtin_cannyHough(self):
        imgOriginal = cv.imread(self.img)
        img = cv.cvtColor(imgOriginal, cv.COLOR_BGR2GRAY)       # convert color image into grey-scale image 
        cv.imshow("Original", imgOriginal)
        img = cv.blur(img, (5,5))                       # blurring image reduces noise
        # img = cv.GaussianBlur(img,(5,5),0)                      # Sobel of Gaussian, SoG
        img = cv.GaussianBlur(img,(5,5),0)     

        imgCanny = cv.Canny(img, 150, 200, L2gradient=5)
        lines = cv.HoughLinesP(imgCanny, 1, np.pi / 180, 50, None, 50, 10)
        cdstP = cv.cvtColor(imgCanny, cv.COLOR_GRAY2BGR)

        imgCannyHough = np.copy(cdstP)
        imgHoughP = np.copy(imgOriginal)
        cv.imshow("Canny Edge", imgCanny) 

        if lines is not None:
            for i in range(0, len(lines)):
                l = lines[i][0]
                cv.line(imgCannyHough, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
                cv.line(imgHoughP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

        cv.imshow("Canny w/ Hough", imgCannyHough)
        cv.imshow("Final", imgHoughP)        

        self.__closeAll()

    def gaussianBlur(self):
        img = cv.imread(self.img)
        img = cv.GaussianBlur(img, (5,5), 0)
        cv.imshow("Gaussian image", img)

        self.__closeAll()

    def showImg(self):
        img = cv.imread(self.img)
        cv.imshow("Image", img)

        self.__closeAll()

    def __closeAll(self):
        while True:
            k = cv.waitKey(0)
            if k == ord('q'):
                break        

        cv.destroyAllWindows()            