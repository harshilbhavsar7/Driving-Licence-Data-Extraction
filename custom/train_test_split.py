import os
from pathlib import Path
import random
import shutil

import pdb 

image_path =r"C:\Harshil\Study\Semester_2\AI_ML_Lab\DL_Dataset\final_data_v1\images"
annot_path =r"C:\Harshil\Study\Semester_2\AI_ML_Lab\DL_Dataset\final_data_v1\labels"

des_image = r"C:\Harshil\Study\Semester_2\AI_ML_Lab\DL_Dataset\final_data_v1\final_images"
des_annot = r"C:\Harshil\Study\Semester_2\AI_ML_Lab\DL_Dataset\final_data_v1\final_labels"


files = os.listdir(image_path)

files_shuffled=random.sample(files,len(files))

train,test,val = 0.8,0.1,0.1


train_num = int(train*len(files))
for i in files[:train_num]:
    # pdb.set_trace()
    shutil.copy(os.path.join(image_path,i),os.path.join(des_image,'train'))
    shutil.copy(os.path.join(annot_path,os.path.splitext(i)[0]+'.txt'),os.path.join(des_annot,'train'))
    
test_num = int(test*len(files))
for i in files[train_num:train_num+test_num]:
    # f.write(os.path.splitext(i)[0]+'\n')
    shutil.copy(os.path.join(image_path,i),os.path.join(des_image,'test'))
    shutil.copy(os.path.join(annot_path,os.path.splitext(i)[0]+'.txt'),os.path.join(des_annot,'test'))
        
val_num = int(val*len(files))
for i in files[train_num+test_num:train_num+test_num+val_num]:
    # f.write(os.path.splitext(i)[0]+'\n')
    shutil.copy(os.path.join(image_path,i),os.path.join(des_image,'val'))
    shutil.copy(os.path.join(annot_path,os.path.splitext(i)[0]+'.txt'),os.path.join(des_annot,'val'))


print('Train Files :::: {}'.format(train_num))
print('Test Files :::: {}'.format(test_num))
print('Validation Files :::: {}'.format(val_num))
print('Total :::: {}'.format(len(files)))