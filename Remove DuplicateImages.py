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
Images = os.listdir("../../TempPictures")
#print(Images)

##Trying to start a threading before this loop, won't work as results from each y comparison impacts the next
for y in range(len(Images)):
    ##open base image
    img1 = cv.imread("../../TempPictures/"+Images[y], cv.IMREAD_GRAYSCALE)

    ##For every element in Duplicate array, check if Image Y is already in there
    ItemInDuplicates = False;
    for z in Duplicates:
       ## Check if Image Y is already in elemnt Z of Duplicates
       if Images[y] in z:
          ItemInDuplicates = True;
          
    #If Image y is not in duplicate array already, add it to the Sorted Array
    if ItemInDuplicates == False:
       Sorted.append(Images[y])

    ## Could try threading here, as the comparison agaisnt each x is independent, dosen't matter what position x when doing comparison as it won't impact comparison agaisnt next X
    for x in range(y+1,len(Images)):
        #Check if image is being compared agaisnt self and that item hasn't already been found to be in duplicates
        if Images[y] != Images[x] and ItemInDuplicates != True:
            try:
               #open Comparison image
               img2 = cv.imread("../../TempPictures/"+Images[x], cv.IMREAD_GRAYSCALE)
            
               ######compare Images########
               if skip == False:
                   #Check if Image size/shapes are same
                   if img1.shape == img2.shape:
                       #Perform mean squared error comparison
                       error = mse(img1, img2)
                       #Append to duplicate list to update jagged array
                       if error < 1:
                          Duplicates.append([Images[y],Images[x]])
            except:
               print("Can't compare shape of item " + Images[y] + " and item " + Images[x])

#Move itmes on Duplicates List out of folder
#os.rename("C:\files\example.txt", "C:\backup\example.txt")
for i in range(len(Sorted)):
   os.rename("../../TempPictures/"+Sorted[i],"../Sorted/"+Sorted[i])

