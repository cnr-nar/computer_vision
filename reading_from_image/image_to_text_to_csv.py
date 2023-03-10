import cv2
import pandas as pd
import easyocr
from array import *
import csv

reader = easyocr.Reader(['en'])
from pathlib import Path  

list_el = []

for i in range(0,236):
    path = "images\image_"+str(i)+".jpg"
    result = reader.readtext(path, paragraph= False)
    df = pd.DataFrame(result)
    list_el.append(df[1])
    print("image"+str(i)+"done")

df_out = pd.DataFrame(list_el)
filepath = Path('to_csv/read_images.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df_out.to_csv(filepath)  