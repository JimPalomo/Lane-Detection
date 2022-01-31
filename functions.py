# Erik Resendiz & Jim Palomo
# ECE 415 | Project

# Edge Detection Operator Functions

from lanedetection import LaneDetection

def other(userInput, LD):
    if userInput == "0":
        LD.gaussianBlur()
    elif userInput == "1":
        LD.showImg()
    elif userInput == "2":
        LD.info()

def default(userInput, LD):
    if userInput == "0":
        LD.default_prewitt()
    elif userInput == "1":
        LD.default_sobel()
    elif userInput == "2":
        LD.default_canny()
    elif userInput == '3':
        LD.default_laplacian()

def builtin(userInput, LD):
    if userInput == "0":
        LD.builtin_prewitt()
    elif userInput == "1":
        LD.builtin_sobel()
    elif userInput == "2":
        LD.builtin_canny()
    elif userInput == "3":
        LD.builtin_laplacian()
    elif userInput == "4":
        LD.builtin_cannyHough()