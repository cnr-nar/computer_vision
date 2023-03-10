import cv2
import pandas as pd
import easyocr
from array import *
import csv

reader = easyocr.Reader(['en']) # Image to text trained frame
from pathlib import Path  

list_el = []
# Gets Images 
for i in range(0,236): #This just manually checked image number
    path = "images\image_"+str(i)+".jpg"
    result = reader.readtext(path, paragraph= False)
    df = pd.DataFrame(result)
    list_el.append(df[1])
    print("image"+str(i)+"done")

# creates a dataFrame to write datas in a csv file
df_out = pd.DataFrame(list_el) 
filepath = Path('to_csv/read_images.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df_out.to_csv(filepath)  
