#https://gis.stackexchange.com/questions/401797/how-to-process-list-of-gcp-points-in-gdal-in-python
import pandas as pd
from osgeo import gdal
import os,sys

www=open("train.csv","w")
www.writelines("img,d0x,d0y,d1x,d1y,d2x,d2y,d3x,d3y\n")

ls=list()
for i in range(1,105,1):
    s=str(i).rjust(3,'0')
    if(i<42 and i>39): #空
        continue
    if(i<=83 and i>=81): #空
        continue
    if(i==50 or i==51 or i==22 or i==104 or i==101 or i==88 or i==38): #不良資料
        continue
    if(i==2):
        ls.append(s+"a")
        ls.append(s+"b")
    else:
        ls.append(s)

for i in ls:
    print(i)
    # Read the coordinates in the CSV file
    names = "JM50K_1924_"+i
    f=pd.read_csv("GCPs/"+names+".tif.points")
    keep_col = ['mapX','mapY','pixelX', 'pixelY', 'enable']
    new_f = f[keep_col]
    df = new_f.drop(columns=['enable'])
    col=['mapX','mapY', 'pixelX','pixelY']
    modified_df = df[col]
    modified_df['pixelY'] = modified_df['pixelY'] *(-1) 

    # Create an empty GCP list
    ss=names+".jpg"
    gcp_list=list()
   
    # GCP coordinates list  
    for index, rows in modified_df.iterrows():
      
        gcps = gdal.GCP(rows.mapX, rows.mapY, 1, rows.pixelX, rows.pixelY )
        #gcp_list.append(gcps)
        print(names,gcps)
      
        gcp_list.append((int(rows.pixelX),int(rows.pixelY)))
    mn, mx=0,0
    for i in range(4):
        if gcp_list[i][0]+gcp_list[i][1] <= gcp_list[mn][0]+gcp_list[mn][1]:
            mn=i
    for i in range(4):
        if gcp_list[i][0]+gcp_list[i][1] >= gcp_list[mx][0]+gcp_list[mx][1]:
            mx=i
    set1={0,1,2,3}
    set1.remove(mn)
    set1.remove(mx)
    second=min(set1)
    third=max(set1)
    if gcp_list[second][0]>gcp_list[third][0]:
        second,third=third,second
    gcp_list2=[gcp_list[mn],gcp_list[second],gcp_list[third],gcp_list[mx]]
    for i,j in gcp_list2:
        ss+=","+str(i)+","+str(j)
    www.writelines(ss+'\n')
www.close()
