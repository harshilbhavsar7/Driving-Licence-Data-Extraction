# Libraries for Object Detection
import torch
from PIL import Image
import imagehash
import cv2
import os
import datetime  
import json
import numpy as np

from custom.runOCR import runOCR
from custom.global_data import checkpoint_file,class_names
from custom.storing import store_image,store_face

predicts=[]

def init():
	try :
		global model
		model = torch.hub.load('ultralytics/yolov5', 'custom', path=checkpoint_file)
		print("success")
	except Exception as e:
		print('exception')
		print(e)

def class_to_label(x):
	try:
		class_name = class_names[int(x)]
		return class_name
	except Exception as e:
		print(e)


def process_entity(image,x1, y1, x2, y2, acc, class_name):	
	output= runOCR(image,x1,y1,x2,y2,class_name)
	output=output.replace("\n\f",'')
	output=output.replace("\n\n",'')
	output=output.replace("\n",'')
	output=output.replace("~",'')
	output=output.replace("|",'')
	return output

def process_face(image,image_name, x1, y1, x2, y2, acc, class_name):	
	stored_path= store_face(image,image_name,x1,y1,x2,y2,acc,class_name)
	return stored_path



def run(img):
	try:
		ocrdict={}
		ocrdict.clear()
		dict_cat={}
		dict_cat.clear()
		hashvalue= imagehash.average_hash(Image.open(img))
		image_name=os.path.basename(img)
		original=cv2.imread(img)
		image=cv2.imread(img)
		predictions = model(img)
		labels,cord =predictions.xyxyn[0][:, -1].numpy(),predictions.xyxyn[0][:, :-1].numpy()
		x_shape, y_shape = image.shape[1],image.shape[0]
		bad_count=0
		classes_check=[]
		predicts.clear()
		for i in range(len(labels)):
			row = cord[i]
			row= np.append(row,labels[i])
			if row[4] >= 0.2:
				x1, y1, x2, y2, acc, class_name= int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape),row[4],class_to_label(row[5])
				if class_name not in classes_check:
					classes_check.append(class_name)
					predicts.append([x1, y1, x2, y2, acc, class_name])
					# if acc<0.50:
					# 	bad_count= bad_count+1
					if class_name=="face":
						facepath = process_face(image,image_name,x1, y1, x2, y2, acc, class_name)
						# ocrdict.update(table = dict_cat)
						ocrdict[class_name]=facepath
					else:
						output = process_entity(image,x1, y1, x2, y2, acc, class_name)
						ocrdict[class_name]=output
				else:
					continue

		ocrdict.update(dict_cat)
		store_image(img,original,image,image_name,hashvalue,predicts,ocrdict)

		return ocrdict

	except Exception as e:
		print(e)

