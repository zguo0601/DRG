from selenium import webdriver
from common.base import Base
from pages.yy_Loginfuc import LoginDrg
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'E:\tesseract-ocr\tesseract.exe'  # 执行的路径
image1 = Image.open('E:\\web_auto\\pages\\5.jpg')  # 识别的图片路径
text1 = pytesseract.image_to_string(image1)  # 转换成文本
print(text1)
print(text1)
print(text1)
print(text1)
print(text1)
print(text1)
print(text1)



























