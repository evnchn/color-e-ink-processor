# Color e-paper Processor
Code to pre-process images for particular e-paper panels. The resulting image should then be possible to be uploaded onto the color e-paper panel 

## Panel identification
The panel may go under various names. Key features are:
- "I80" connector
- Alternating RGB pixels in the following format:
```
RBGRBGRBG
GRBGRBGRB
BGRBGRBGR
```

## Panel sources
Here are some potential sources:
https://www.good-display.com/product/89/

-> https://www.good-display.com/product/365.html I own it. Tested working so far

https://shopkits.eink.com/product-category/color-epaper-modules/

## Usage
Currently this is in early alpha for proof-of-concept and exists as a script which requires user editing. ```tarwidth``` and ```tarheight``` should be edited for other panels, as well as the dithering logic. It depends on ImageMagick "convert.exe" for use in Windows platforms. 

## Todo
- Code refactoring and variable naming cleanup
- Make into package
- Cross-platform calling of ImageMagick
- Adapting for other panels
  - If you are in possession of other panels, please try and contact me
