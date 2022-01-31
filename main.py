# Erik Resendiz & Jim Palomo
# ECE 415 | Project

import os

from functions import *
from lanedetection import LaneDetection

def main():
    # create a list of the images in the images dir
    imageList = os.listdir("images/")

    # print out list of applicable images
    print("List of Image:")
    for i in range(len(imageList)):
        print(f"  {i} : {imageList[i]}")
    print()

    # user options
    defaultStr = ["Prewitt", "Sobel", "Canny", "Laplacian"]
    builtinStr = ["Prewitt", "Sobel", "Canny", "Laplacian", "Canny w/ Hough Line Transform"]
    otherStr = ["Gaussian Blur", "Show Image", "Image Info"]

    # create a Lane Detection class object
    userImg = input('Choose an Image (0-5): ')
    print()
    LD = LaneDetection(f"images/{imageList[int(userImg)]}")
    
    opType = input('Choose the type of operator ("d", "b", "o"), "h" for help, or "q" to quit: ')
    
    while opType != 'q':
        if opType == 'h':
            opType = input('\nChoose from the following type of operators to obtain a list of operators available:\n  d : Default\n  b : Builtin\n  o : Other\n  q to quit\n')
        elif opType == 'd':
            for i in range(len(defaultStr)):
                print(f"  {i} : {defaultStr[i]}")
            
            userOp = input('\nChoose from the listed type of operators (0-3): ')
            default(userOp, LD)
            break

        elif opType == 'b':
            for i in range(len(builtinStr)):
                print(f"  {i} : {builtinStr[i]}")
                
            userOp = input('\nChoose from the listed type of operators (0-4) [Recommended to use 4]: ')
            builtin(userOp, LD)
            break

        elif opType == 'o':
            for i in range(len(otherStr)):
                print(f"  {i} : {otherStr[i]}")

            userOp = input('\nChoose from the listed type of operators (0-2): ')
            other(userOp, LD)
            break
        
        else:
            opType = input('Invalid Command. Choose the type of operator ("d", "b", "o"), "h" for help, or "q" to quit: ')

if __name__ == "__main__":
    main()
