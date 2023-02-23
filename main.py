import pywinctl
import os
import pyautogui
import PIL
import os  # from native modules
import fitz  # from PyMuPDF
import pytesseract  # from pytesseract
import cv2  # from Opencv
import argparse
import io  # from native modules
from PIL import Image, ImageFile  # from Pillow
from colorama import Fore  # from native modules
import platform  # from native modules
import time
import webbrowser

# get screensize
# x,y = pyautogui.size()
# print(f"width={x}\theight={y}")

# x2,y2 = pyautogui.size()
# x2,y2=int(str(x2)),int(str(y2))
# print(x2//2)
# print(y2//2)

# find new window title
# z1 = pywinctl.getAllTitles()
# time.sleep(1)
# print(len(z1))
# # test with pictures folder
# os.system("open monitor-1.png")
# time.sleep(1)
# z2 = pywinctl.getAllTitles()
# print((z2))
# time.sleep(1)
# z3 = [x for x in z2 if x not in z1]
# z3 = ''.join(z3)
# time.sleep(3)

# print(pywinctl.getAllTitles())

# also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"

# quarter of screen screensize
x = 700
y = 800
# my.resizeTo(x,y)
# top-left

# RUN ONLY ON FIRST RUN
# my = pywinctl.getWindowsWithTitle('Movie Recording')[0]
# my.moveTo(0, 0)
# time.sleep(0.1)
# my.activate()
# time.sleep(0.1)

# save screenshot
p = pyautogui.screenshot(region=(100,600,x,y))
p.save(r'p.png')

# edit screenshot
# im = PIL.Image.open('p.png')
# im_crop = im.crop((100, 400, x, y+400))
# im_crop.save('p.png', quality=100)

# # close window
# time.sleep(1)
# my.close()

# TESSERACT#

 
#We then read the image with text
images=cv2.imread("p.png")
 
#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
 
#checking whether thresh or blur
# if args["pre_processor"]=="thresh":
cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
# if args["pre_processor"]=="blur":
#     cv2.medianBlur(gray, 3)
     
#memory usage with image i.e. adding image to memory
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open('57214.png'))
os.remove(filename)
# print(text)
 
# show the output images
# cv2.imshow("Image Input", images)
# cv2.imshow("Output In Grayscale", gray)
# cv2.waitKey(0)

# Processing and API Call
question, answers = text.split('?')
question = question.replace('\n', ' ') + "?"

url = "https://www.google.co.in/search?q=" + question
webbrowser.open_new(url)



