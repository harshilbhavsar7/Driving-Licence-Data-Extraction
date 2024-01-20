from custom.create_today_folder import create_today_folder
from custom.generate_voc import generate_xml

import cv2
import os
import json

def store_image(imgpath,original,image,image_name,hashvalue,predicts,ocrdict):
    try :
        output_dir="./api_output"
        jsondata=json.dumps(ocrdict)  
        folder=create_today_folder(output_dir)
        predictionpath=os.path.join(folder,os.path.splitext(image_name)[0]+'_output.jpg')
        cv2.imwrite(predictionpath,image)
        generate_xml(original,image,image_name,predicts,folder)
        # insert_table(hashvalue,imgpath,predictionpath,jsondata)                   
    except Exception as e:
        print(e)


def store_face(image,image_name,x1,y1,x2,y2,acc,class_name):
    try :
        output_dir="./api_output"
        folder=create_today_folder(output_dir)
        roi=image[y1:y2,x1:x2]
        predictionpath=os.path.join(r'C:\Harshil\Study\Semester_2\AI_ML_Lab\Final_Project\Driving_Licence_Extract_API\static',os.path.splitext(image_name)[0]+'_face_output.jpg')
        image_name= os.path.basename(predictionpath)
        print(predictionpath)
        cv2.imwrite(predictionpath,roi)
        return image_name
    except Exception as e:
        print(e)


def store_excel(df):
    try :
        output_dir="./api_output"  
        folder=create_today_folder(output_dir)
        outputpath=os.path.join(folder,'final_output.xlsx')
        # df.to_excel(outputpath,index = False)
        df.to_excel(outputpath)
    except Exception as e:
        print(e)