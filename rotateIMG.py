import cv2
import os
import skimage
from PIL import Image
import math

dirpath = './tmpIMG1'
newpath = './tmpIMG2'

filelist = os.listdir(dirpath)

n=0
for line in filelist:
    if (line[0] == '.'):
        continue
    n+=1
    line = line.strip()
    fullfilepath = os.path.join(dirpath, line)
    img = Image.open(fullfilepath)
    cornerstr = line.split('_')[-2]
    corner = float(cornerstr)/math.pi*180
    print (n, corner)
    imgnew = img.rotate(corner-90)
    newfullfilepath = fullfilepath.replace(dirpath, newpath)
    newfullfilepath = newfullfilepath.replace(cornerstr, 'rot')
    imgnew.save(newfullfilepath)