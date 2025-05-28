#Actividad I2C

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
padding = -2
top = padding
bottom = height-padding


def imprimeNombres():
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    draw.text((0, top), 'Dario Sanchez Perzabal', font=font, fill=270)
    draw.text((0, top+8), 'Santiago Gomez Ochoa', font=font, fill=270)
    disp.image(image)
    disp.show()
    time.sleep(5)
    disp.fill(0)

    disp.show()
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.text((0, top), 'Escribe un mensaje: ', font=font, fill=270)
    disp.image(image)
    disp.show()
    mensaje = input()
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.text((0, top), mensaje, font=font, fill=270)
 
    disp.image(image)
    disp.show()
    
imprimeNombres()

