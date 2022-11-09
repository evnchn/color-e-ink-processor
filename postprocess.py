import numpy as np
from PIL import Image, ImageOps
import math
from fractions import Fraction
tarwidth = 1448
tarheight = 1072
from numba import jit
new_height = tarheight
new_width = tarwidth






img = Image.open('[EDIT THIS].jpg').convert('RGB')




lratio = Fraction(tarwidth, img.size[0])
wratio = Fraction(tarheight, img.size[1])

print(lratio)
print(wratio)

minratio = min(lratio,wratio)

img = img.resize([int(i*minratio) for i in img.size])


leftpad = (tarwidth-img.size[0])//2

toppad = (tarheight-img.size[1])//2

rightpad = tarwidth-leftpad-img.size[0]
bottompad = tarheight-toppad-img.size[1]

print(leftpad,toppad,rightpad,bottompad)

img = ImageOps.expand(img, (leftpad,toppad,rightpad,bottompad))

img.save("intermediate.png")



print("Dithering...")
import subprocess

subprocess.call("convert intermediate.png -channel RGB -separate -dither FloydSteinberg -colors 16 -combine -depth 4 intermediate2.png".split(" "))

img = Image.open('intermediate2.png').convert('RGB')

#img = add_salt_and_pepper(img,0.2)

print("Dithering DONE")
img.size


arr = np.array(img) # 640x480x4 array

print(arr)

input()

# arr = -np.floor_divide(arr,255)*255+255

#arr = np.floor_divide(arr,255)*255

arr = np.floor_divide(arr+0,17)*17

print(arr)

reds = arr[:,:,0].reshape(-1)[0::3]
greens = arr[:,:,1].reshape(-1)[2::3]



blues = arr[:,:,2].reshape(-1)[1::3]


greens = np.pad(greens, (0, reds.size-greens.size), 'constant')

#new_im = ImageOps.expand(im, padding)

print(arr.shape)
print(reds.shape)
print(greens.shape)
print(blues.shape)

print(reds)

# allcolorsstacked = np.vstack((reds,blues,greens))

#allcolorsstacked = np.vstack((greens,reds,blues))

allcolorsstacked = np.vstack((reds,blues,greens))

print(allcolorsstacked)

#RRRRRR
#BBBBBB
#GGGGGG

allcolorsstackedT = allcolorsstacked.T

print(allcolorsstackedT)

allcolorsstackedI = allcolorsstackedT.reshape(-1)



allcolorsstackedI = np.delete(allcolorsstackedI, -1)



allcolorsreshaped = allcolorsstackedI.reshape(tarheight, tarwidth)



print(allcolorsreshaped.shape)

allcolorsreshaped = allcolorsreshaped.T

for i, v in enumerate(range(0,256,11)):

    allcolorsreshaped[i] = np.full(allcolorsreshaped[0].shape, v)
    
'''    
allcolorsreshaped[allcolorsreshaped.shape[0]//2] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//2]

allcolorsreshaped[allcolorsreshaped.shape[0]//4] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//4]

allcolorsreshaped[allcolorsreshaped.shape[0]//4*3] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//4*3]
'''
allcolorsreshaped = allcolorsreshaped.T


print(allcolorsreshaped.T)
#RBG
#RBG
#RBG
#RBG
#RBG
#RBG
im = Image.fromarray(np.uint8(allcolorsreshaped),'L')

im = im.resize([2*i for i in im.size], Image.NEAREST)

#im.show()
im = im.save("geeks.bmp")
input()

#arr[20, 30] # 4-vector, just like above


