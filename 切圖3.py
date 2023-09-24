#xmnn, ymnn,xmxn,ymxn=318 547 212 390
from PIL import Image
import pandas as pd
import os, sys,random

www=open("fin.csv","w")
www.writelines("img, px, py\n")

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_path = "split_images3"
if image_path not in os.listdir():
    os.mkdir(image_path)
    print("folder created")

data=pd.read_csv("estimatedContour.csv")
od=pd.read_csv("train.csv")
now=0
aaa=40
bbb=210
sc=256
for i in range(int(data.shape[0])):
    imn=str(data.iloc[i][0])
    im = Image.open(imn)
    width, height = im.size
    left,right,up,down=data.iloc[i].left,data.iloc[i].right,data.iloc[i].up,data.iloc[i].down
    #left-up
    xx,yy=aaa,aaa
    box = (left-xx,up-yy,left+sc-xx, up+sc-yy)
    a = im.crop(box)
    a.save(str(image_path+"/"+imn[:-4]+"_0.jpg"))
    s=f"{str(imn[:-4]+'_0.jpg')},{od.iloc[i].d0x-left+xx},{od.iloc[i].d0y-up+yy}\n"
    print(s)
    www.writelines(s)
    #left-down
    xx,yy=aaa,bbb
    box = (left-xx,down-yy,left+sc-xx, down+sc-yy)
    a = im.crop(box)
    a.save(str(image_path+"/"+imn[:-4]+"_1.jpg"))
    s=f"{str(imn[:-4]+'_1.jpg')},{od.iloc[i].d1x-left+xx},{od.iloc[i].d1y-down+yy}\n"
    print(s)
    www.writelines(s)
    #right-up
    xx,yy=bbb,aaa
    box = (right-xx,up-yy,right+sc-xx, up+sc-yy)
    a = im.crop(box)
    a.save(str(image_path+"/"+imn[:-4]+"_2.jpg"))
    s=f"{str(imn[:-4]+'_2.jpg')},{od.iloc[i].d2x-right+xx},{od.iloc[i].d2y-up+yy}\n"
    print(s)
    www.writelines(s)
    #right-down
    xx,yy=bbb,bbb
    box = (right-xx,down-yy,right+sc-xx, down+sc-yy)
    a = im.crop(box)
    a.save(str(image_path+"/"+imn[:-4]+"_3.jpg"))
    s=f"{str(imn[:-4]+'_3.jpg')},{od.iloc[i].d3x-right+xx},{od.iloc[i].d3y-down+yy}\n"
    print(s)
    www.writelines(s)
www.close()
