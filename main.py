import cv2 
import numpy as np

img = cv2.imread('star.png')

height , width , _ = img.shape

cv2.imshow(img)