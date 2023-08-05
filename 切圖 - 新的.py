#xmnn, ymnn,xmxn,ymxn=318 547 212 390
from PIL import Image
import pandas as pd
import os, sys,random

www=open("train2.csv","w")
www.writelines("img, px, py\n")

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_path = "split_images2"
if image_path not in os.listdir():
    os.mkdir(image_path)
    print("folder created")

data=pd.read_csv("train.csv")
now=0
for i in range(data.shape[0]):
    im = Image.open(data.iloc[i][0])
    width, height = im.size
    for j in range(1,9,2):
        x,y=data.iloc[i][j],data.iloc[i][j+1]
        xx = random.randint(20,235)
        yy = random.randint(20, 235)
        box = (x-xx,y-yy,x+256-xx, y+256-yy)
        a = im.crop(box)
        a.save(image_path+"/"+str(now)+".jpg")
        s=f"{now}.jpg,{xx},{yy}\n"
        print(s)
        www.writelines(s)
        now+=1
www.close()
