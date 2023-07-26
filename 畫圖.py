import cv2
import pandas as pd
s="JM50K_1924_"+input()+".jpg"
data=pd.read_csv("train.csv")
mxx=0
mxy=0
for i in range(data.shape[0]):  
    img=cv2.imread(data.iloc[i][0])
    mxx=max(img.shape[1],mxx)   
    mxy=max(img.shape[0],mxy)
    if(data.iloc[i][0]==s):
        mxx=max(img.shape[1],mxx)
        mxy=max(imh.shape[0],mxy)
        print("ya")
        
        print(img.shape)
        ls=list()
        for j in range(1,9,2):
            point=(data.iloc[i][j],data.iloc[i][j+1])
            ls.append(point)
            cv2.circle(img, point, 10, (0,0,255), 4)
            cv2.circle(img, point, 2, (0,0,255), 3)
        for i in range(4):
            point=ls[i]
            minx=point[0]//500*500
            maxx=min(minx+500,img.shape[1])
            miny=point[1]//500*500
            maxy=min(miny+500,img.shape[0])
            print(minx,maxx,miny,maxy,img.shape[1],img.shape[0])
            cv2.imshow(str(i),img[miny:maxy-2,minx:maxx-2])

print(mxx,mxy)
