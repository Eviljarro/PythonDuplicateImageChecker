import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

def mse(img1, img2):
   h, w = img1.shape
   diff = cv.subtract(img1, img2)
   err = np.sum(diff**2)
   val = err/(float(h*w))
   return val

def element_exists(lst, element):
  # Try to get the index of the element in the list
  try:
    lst.index(element)
  # If the element is found, return True
    return True
  # If a ValueError is raised, the element is not in the list
  except ValueError:
  # Return False in this case
    return False

#Variables
Duplicates = []
Sorted = []
skip = False;

##List all files in Images Directory
Images = os.listdir("Images")
print(Images)

for y in range(len(Images)):
    ##open base image
    img1 = cv.imread("Images/"+Images[y], cv.IMREAD_GRAYSCALE)

    ##Store copy of Image y in original array if its not already in the duplicate array
    #if Images[y] not in Duplicates:
    #   Sorted.append(Images[y])
    
    for x in range(y+1,len(Images)):
        #Check if image is being compared agaisnt self
        if Images[y] != Images[x]:
            #open Comparison image
            img2 = cv.imread("Images/"+Images[x], cv.IMREAD_GRAYSCALE)
            
            #Check if image is already in Duplicate list, if so skip comparison
            skip = False
            for z in Duplicates:
                if Images[x] in z:
                    skip = True
                    
            #Add Image to the seperate sorted list, but it must include the first version of a duplicate image it comes across

            ######compare Images########
            if skip == False:
                #Check if Image size/shapes are same
                if img1.shape == img2.shape:
                    #Perform mean squared error comparison
                    error = mse(img1, img2)
                    #open chart if duplicate and display
                    #print("Image matching Error between the two images:", error)
                    #plt.figure()
                    #plt.imshow(img1)
                    #plt.figure()
                    #plt.imshow(img2)
                    #plt.show()
                    
                    cv.waitKey(0)
                    cv.destroyAllWindows()
                    #Append to duplicate list to update jagged array
                    if error < 1:
                       Duplicates.append([Images[y],Images[x]])
                #else:
                #    print("No Match")

print(Duplicates)
print(len(Duplicates))

print(Sorted)
print(len(Sorted))


#Move itmes on Duplicates List out of folder


