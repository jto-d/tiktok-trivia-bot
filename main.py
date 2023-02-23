import pywinctl
import os
import pyautogui
import os  # from native modules
import pytesseract  # from pytesseract
import cv2  # from Opencv
from PIL import Image
import webbrowser

# create screensize (run screen_setup.py first)
x = 700
y = 800

# save screenshot
p = pyautogui.screenshot(region=(100,600,x,y))
p.save(r'p.png')

# TESSERACT

# read image using cv2
images=cv2.imread("p.png")
 
# convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
 
# use thresh

#checking whether thresh or blur
# if args["pre_processor"]=="thresh":
cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
# if args["pre_processor"]=="blur":
#     cv2.medianBlur(gray, 3)
     
# memory usage with image i.e. adding image to memory
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open('57214.png'))
os.remove(filename)
# print(text)
 
# show the output images
# cv2.imshow("Image Input", images)
# cv2.imshow("Output In Grayscale", gray)
# cv2.waitKey(0)

# question processing
question, answers = text.split('?')
question = question.replace('\n', ' ') + "?"

# search google
url = "https://www.google.co.in/search?q=" + question
webbrowser.open_new(url)



