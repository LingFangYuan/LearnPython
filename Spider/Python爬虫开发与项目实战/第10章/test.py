# -*- coding: UTF-8 -*_
from PIL import Image
from pytesseract import *
import PIL.ImageOps
import turtle as t
def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    print(w, h)
    t.Turtle().screen.delay(0)
    t.setup(w+100, h+100)
    t.penup()
    t.goto(-w, h)
    t.seth(0)
    
    for y in range(0,h):
        flag = 0
        flag1 = 0
        for x in range(0,w):
            t.penup()
            t.goto(x-w, h-y)
            t.pendown()
            if pixdata[x, y] == 0:
                if flag == 0:
                    flag1 += 1
                flag = 1
                t.fd(1)
            else:
                flag = 0
                if flag1 // 2 == 1:
                    t.fd(1)
    t.done()
    return img


im = Image.open('weibo.png')
#图片的处理过程
im = im.convert('L')
#像素点处理 二值图像，非黑即白 相当于去噪操作
binaryImage = im.point(initTable(), '1')
#模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度 
im1 = binaryImage.convert('L')
im1 = depoint(im1)
# 反转颜色
# im2 = PIL.ImageOps.invert(im1)
# im3 = im2.convert('1')
# im4 = im3.convert('L')
#将图片中字符裁剪保留
# box = (30,10,90,28) 
# region = im4.crop(box)  
#将图片字符放大
#out = im1.resize((120,38)) 
asd = pytesseract.image_to_string(im4)
print (asd)

print (im4.show())