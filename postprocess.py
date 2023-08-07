import numpy as np
from PIL import Image, ImageOps, ImageEnhance
import subprocess

def do_image_generation(tarwidth, tarheight, filename):

    img = Image.open(filename).convert('RGB').rotate(180)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)

    img = ImageOps.pad(img, (1448,1072),color=(255,255,255))

    img.save("intermediate.png")

    print("Dithering...")

    subprocess.call("convert intermediate.png -channel RGB -separate -dither FloydSteinberg -colors 16 -combine -depth 4 intermediate2.png".split(" "))

    img = Image.open('intermediate2.png').convert('RGB')

    #img = add_salt_and_pepper(img,0.2)

    print("Dithering DONE")

    arr = np.array(img) # 640x480x4 array

    #input()

    # arr = -np.floor_divide(arr,255)*255+255

    #arr = np.floor_divide(arr,255)*255

    arr = np.floor_divide(arr+0,17)*17

    print(arr)

    reds = arr[:,:,0].reshape(-1)[0::3]
    greens = arr[:,:,1].reshape(-1)[2::3]
    blues = arr[:,:,2].reshape(-1)[1::3]


    greens = np.pad(greens, (0, reds.size-greens.size), 'constant')

    #new_im = ImageOps.expand(im, padding)

    # by experimentation, may change for different panel models
    allcolorsstacked = np.vstack((reds,blues,greens))

    ## now it is: 
    #RRRRRR
    #BBBBBB
    #GGGGGG

    allcolorsstackedT = allcolorsstacked.T

    allcolorsstackedI = allcolorsstackedT.reshape(-1)

    allcolorsstackedI = np.delete(allcolorsstackedI, -1)

    allcolorsreshaped = allcolorsstackedI.reshape(tarheight, tarwidth)

    # OPTION: uncomment this and below to add vertical stripes (legacy, unused)
    # allcolorsreshaped = allcolorsreshaped.T
    ''' # this adds vertical stripes of grayscale
    for i, v in enumerate(range(0,256,11)):

        allcolorsreshaped[i] = np.full(allcolorsreshaped[0].shape, v)
        '''
    '''
    # this adds vertical stripes of inverted image at 1/2, 1/4 and 3/4 width
    allcolorsreshaped[allcolorsreshaped.shape[0]//2] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//2]
    allcolorsreshaped[allcolorsreshaped.shape[0]//4] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//4]
    allcolorsreshaped[allcolorsreshaped.shape[0]//4*3] = 255 - allcolorsreshaped[allcolorsreshaped.shape[0]//4*3]
    '''
    # OPTION: uncomment this and above to add vertical stripes (legacy, unused)
    # allcolorsreshaped = allcolorsreshaped.T

    ## by now it is: 

    #RBG
    #RBG
    #RBG

    im = Image.fromarray(np.uint8(allcolorsreshaped),'L')

    im = im.resize([2*i for i in im.size], Image.NEAREST)

    #im.show()
    im = im.save("output.bmp")

    print("Saved to file")
    #input()

    #arr[20, 30] # 4-vector, just like above


