#xmnn, ymnn,xmxn,ymxn=318 547 212 390
from PIL import Image
import pandas as pd
import os, sys

image_path = "spilt_images"
if image_path not in os.listdir():
    os.mkdir(image_path)
    print("folder created")

data=pd.read_csv("train.csv")
for i in range(data.shape[0]):
    im = Image.open(data.iloc[i][0])
    width, height = im.size
    k=0
    for j in range(1,9,2):
        x,y=data.iloc[i][j],data.iloc[i][j+1]
        box = (x-127,y-127,x+129, y+129)
        a = im.crop(box)
        a.save(image_path+"/"+data.iloc[i][0]+"_"+str(k)+".jpg")
        k+=1

