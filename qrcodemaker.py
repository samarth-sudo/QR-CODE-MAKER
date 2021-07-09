import pyqrcode
from pyqrcode import QRCode
import os
import shutil

# String which input the value for QR-code
title = input("Enter the title for QR code-->")
location = input("Enter the Location to save Qr code files--->")
s = input("Enter what you want to convert into QR code---> ")
# create type of files
file_title_svg = title + ".svg"
file_title_png = title + ".png"
file_title_jpeg = title + ".jpeg"
# Creates  QR-code
code = pyqrcode.create(s)
# create and save the file
code.svg(file_title_svg, scale=8)
code.png(file_title_png, scale=10)
code.jpeg(file_title_jpeg, scale=10)
# Place to move
os.mkdir(location+fr"\{title}")
shutil.move(file_title_svg, location+fr"\{title}")
shutil.move(file_title_jpeg, location+fr"\{title}")
shutil.move(file_title_png, location+fr"\{title}")