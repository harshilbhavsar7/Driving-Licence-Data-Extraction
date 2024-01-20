### Abstract 

In government organizations, extracting data from images is challenging. We have identified this problem and decided to extract the data, like a person’s name, address, Driving license number etc, from the driving license like G1, G2, and G or any other country’s license. So it will become easy for the employees; they do not need to add the data manually. This web application will help them to extract the data from the images. They can also download the extracted data in Excel format. 
Initially, we collected the driving license data from some online resources or from our friends and family. After doing the annotations, we tried to train the multiple custom YOLO v5 models. At last, we compared the results of the trained custom models and tried to figure out which model works best for our project . At last, we developed the Flask API so that anyone can upload the license images by using the web app and get the license data. The API can also be modified easily to return JSON response while being in consumption.

### Introduction 
In today’s world, every process is online, from applying for jobs to filing your tax returns online. And for most of these processes, we have to attach our identity proof like a driving license or any other proof. So, most people prefer to upload a driver’s license as proof of identity. And sometimes, for an organization, it is tough to extract those image data into some document and enter them in their database. So, we identified that problem and decided to extract the person’s driving license data from the image like the person’s name, address, driving license number, etc. from any country’s license.  We also developed a web application, so that anyone can upload the license images in the app and get the person’s data in a JSON or excel format.

Having the data extracted from driving license images can help automate the process of verifying and recording personal information. This can be useful in a variety of scenarios, such as when applying for a job, opening a bank account, or renting a car. By automatically extracting the data from the license image, the process can be completed more quickly and accurately, reducing the risk of errors or fraud.

Secondly, extracting data from driving license images can help improve safety on the roads. For example, police officers can use this data to quickly identify drivers who are not legally authorized to drive, or to verify that drivers have the appropriate qualifications and licenses for the vehicles they are operating. Moreover, this project can also help with identity verification and fraud prevention. By comparing the information on the license with other sources of information, such as a national ID database or a credit report, it is possible to identify cases where someone is attempting to use a fake or stolen identity.

We have developed the custom YOLO model to implement this project. We have trained multiple YOLOV5 custom models for this project and chose the one with highest accuracy, precision and recall. To implement this project, we needed the license image data, so we tried to collect some of that from online resources and also from our family and friends. We collected around 100 images of license for our project and did annotations on them by using labelIMG tool , while regularly training yolov5 model on available completed annotations. This allowed us to tweak our annotations side by side by analyzing the model result and doing so helped us to finalize a proper method and classes for our annotations. We also analyzed the annotated text file generated by labelIMG tool to validate the annotations.

### Methods	

In our project, we have used YOLO v5 custom model to train our license image dataset. YOLO, short for "You Only Look Once," is an object detection model introduced in 2016 by Joseph Redmon et al. YOLO uses a single convolutional neural network (CNN) architecture to detect objects in an image, classifying them and localizing their positions with bounding boxes.
The YOLO model divides an input image into a grid and applies convolutional layers to each cell in the grid to predict a set of bounding boxes and class probabilities. Each bounding box predicts the coordinates of the box's center point, its height and width, and a confidence score that represents the model's certainty that an object is present in that box. The class probabilities are predicted for each box, representing the likelihood that the object in that box belongs to a particular class.

One of the main advantages of YOLO over other object detection models is its speed. YOLO can process images in real-time, making it well-suited for applications such as video surveillance and autonomous driving. However, this comes at the cost of lower accuracy compared to some other object detection models, especially for smaller objects.
Since the introduction of the original YOLO model, several versions have been developed with improved accuracy and speed, including YOLOv2, YOLOv3, YOLOv4, YOLOv5, YOLOv6, YOLOv7 and YOLOv8.

### Data set 
* We used license images of three countries in our dataset while doing this project. We collected around 100 scanned license images from online resources and family and friends.
* As the driving license is considered sensitive in nature and may expose a person’s identity we could not find more data instances for our dataset. To include more data, we used online resources such as github and medium. The images contain license of individuals from three different countries i.e. Canada, America and India. Each image contains useful driver information such as full name, family name, license number , gender, address, face, issue date, expiry date.
* So, while creating our image data and doing annotating we chose classes such as name, dob, exp_date, address, sex, issue_date, face, license_number. We used these 8 classes in our annotations as well as training. For annotations we used the LabelIMG tool which is an opensource image annotations tool and is quite easy to setup and use.

### YOLO v5 Model 

YOLO (You Only Look Once) is a popular object detection algorithm that uses a neural network to detect objects in images or videos. YOLO v5 is the latest version of the YOLO series, and it was released in 2020. In this model, the architecture was redesigned to improve the accuracy, speed, and efficiency of the previous versions.

YOLO v5 is a deep neural network that uses a single convolutional neural network (CNN) to simultaneously predict the bounding boxes and class probabilities for the objects in the image. CNN consists of a series of convolutional layers, followed by a set of fully connected layers. The input image is first passed through CNN, which extracts a set of features that are used to predict the object detections.

The architecture of YOLO v5 is based on a scaled-YOLOv4 architecture, with some modifications to improve the performance. The model uses a CSP (cross-stage partial) backbone, which is a type of residual network that reduces the computational cost and improves the accuracy. The CSP backbone is made up of multiple convolutional blocks, which are connected in a cross-stage partial manner to reduce the computational cost.

In addition, YOLO v5 uses a novel approach called "anchor-free" object detection, which removes the need for pre-defined anchor boxes that are used in traditional object detection algorithms. Instead, the model predicts the bounding boxes directly, which makes the algorithm more flexible and accurate.

Another improvement in YOLO v5 is the use of a "panoptic" architecture, which combines semantic segmentation and object detection. This allows the model to not only detect the objects in the image, but also segment them into different classes, which improves the accuracy of the detection.

Overall, YOLO v5 is a highly accurate and efficient object detection algorithm that has been used in a variety of applications, including self-driving cars, surveillance systems, and robotics. Its speed and accuracy make it an attractive option for real-time object detection tasks.

![image](https://github.com/harshilbhavsar7/Driving-Licence-Data-Extraction/assets/60917314/433ae91a-5ae7-4a20-846c-4959af1731e9)

In the above diagram, we can see that there are a total of 5 sizes are available in YOLO v5. We have used the YOLOv5s model for our project as we had a small dataset. 
* n for extra small (nano) size model.
* s for small size model.
* m for medium size model.
* l for large size model
* x for extra large size model

### YOLO v8 Model

YOLO v8 model is the latest model. It launched in January 10th, 2023, claiming advancements in structure and architectural changes with better results.  YOLOv8 has a high rate of accuracy measured by COCO and Roboflow 100. YOLOv8 comes with a lot of developer-convenience features, from an easy-to-use CLI to a well-structured Python package. 


The YOLO and YOLOv8 models have a large and growing community in the field of computer vision, which means you can seek assistance from many people when you need guidance. 
YOLOv8 has achieved a strong accuracy of 50.2% mAP on COCO, particularly with the YOLOv8m model. In comparison to YOLOv5, YOLOv8 scored significantly better on the Roboflow 100 dataset, which evaluates model performance on various task-specific domains. Additionally, YOLOv8 provides convenient features for developers, such as a CLI that simplifies training and a Python package that offers a more seamless coding experience. 

YOLOv8 is an anchor-free model, meaning it predicts the center of an object rather than the offset from a known anchor box. During online training, YOLOv8 augments images, including mosaic augmentation, which involves stitching four images together to teach the model to identify objects in new locations, partial occlusion, and against different surrounding pixels. 
The YOLOv8 models have a comparable code structure to YOLOv5, but with new modifications that allow for classification, instance segmentation, and object detection tasks to be supported using the same code routines. The initialization of models still follows the YOLOv5 YAML format, and the dataset format remains unchanged.

As part of experiment, we trained and evaluated the YOLO v8 model, but the accuracy was fluctuating too much and we believe that it was being overtrained while looking at the precision and recall. In the end we decided to use the YOLO v5 model instead.

The YOLOv8 models use comparable code to YOLOv5, but with a novel structure that enables the same code routines to support classification, instance segmentation, and object detection task types.


### Yolo Results:

Generating good results in object detection task often involves training models and generating outputs and then tweaking the hyperparameters and again do the same process. Each iteration required our utmost attention to the class accuracy in each epoch of the training. The final training session involved 200 epochs with around 100 data points of our dataset split in the ration of 80,10,10 ratio in train, test, val respectively. Also, we have used the hyperparameters for the model tuning as below:
```
* lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.5, cls_pw=1.0, obj=1.0, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.0, copy_paste=0.0
```

As defined above we have used the learning rate as 0.01 to avoid overtraining the model and hitting local minima multiple times. We used weight_decay to penalize model training and to generate more sophisticated results. 
The optimizer we used is SGD (stochastic gradient descent) as that can be seen below from yolo model training output.
SGD (lr=0.01) with parameter groups 57 weight(decay=0.0), 60 weight(decay=0.0005), 60 bias 

The model summary is as below:

![image](https://github.com/harshilbhavsar7/Driving-Licence-Data-Extraction/assets/60917314/49081439-94d1-4e78-bd56-8117dcb16481)

### Flask API

For creating our REST API, we have used Flask framework in python. Using Flask, we were able to quickly and easily generate our API. First, we have created a template for uploading single or multiple images as follows:

![image](https://github.com/harshilbhavsar7/Driving-Licence-Data-Extraction/assets/60917314/7417b9d7-adc5-4102-89ca-23f801ff949b)

We stored the templates in templates folder as the flask framework uses this folder to look for the html templates. We have defined our templates in that folder.  All the uploaded images are stored in api_input folder of the API to keep track of the data.

After creating the template, we defined our API functionality, in that we have created a function called upload_file, which handles the POST request method and gets the uploaded images. In this method, all the necessary functionalities are called. First, we initialize our yolo model with our trained custom model. This model is saved in model_checkpoints folder. After initializing our model, we use that model to predict X-Y coordinates of classes from the images by using custom run method developed by us. 


### Tesseract OCR

Tesseract OCR (Optical Character Recognition) is a free and open-source OCR engine developed by Google. It is designed to recognize and extract text from digital images, including scanned documents and photographs.

Tesseract OCR uses machine learning algorithms and neural networks to recognize text in images. It supports more than 100 languages and can detect multiple languages within a single document. It can also recognize text in various formats, such as handwriting, typewritten text, and printed text.

For extracting the text data we have used tesseract OCR for this project. We installed tesseract engine which is open-source and saved its directory. We installed pytesseract and used that module to connect with the locally installed tesseract engine. Using the custom config  of tesseract we then proceed to extract the text from the image by using ROI of class generated through the model output.

For the ‘face’ class we have just stored the face region of the driver in the static folder of our API to display it for the final result.

After getting all the extracted text data of each particular class, we create annotations in VOC xml format for future training. So, each new inference of the model will generate the new image and annotations that can be tweaked and used in future for improvement of the model. Also, we have created a nested dictionary which contains image name as a main key and the predicted classes as the inside dictionary. We stored that dictionary in dataframe and stored it in the excel format in the api_output folder. 

We then sent the final dataframe to render template which uses the dle_result.html template. This template generates dynamic table according to the dataframe size and also displays the image of face of the driver saved in static folder. Finally, all the generated output data will be stored in dynamic folder named as specific date in which the API is up and processing the request i.e if the API is running today, the dynamic functionality in API will generate folder with today’s datetime string and store the output data in it.


### Final generated output is as below:


![image](https://github.com/harshilbhavsar7/Driving-Licence-Data-Extraction/assets/60917314/5c07f3ee-f858-4397-b6a1-13fa0df208bd)


### Future Work and Conclusions 

There are several potential areas for future work in driving license data extraction using the YOLOv5 model. Here are a few possibilities:
* Improving accuracy: While YOLOv5 is known for its speed and accuracy, there is always room for improvement. Researchers could explore different ways to optimize the model's performance, such as by fine-tuning hyperparameters, adjusting the architecture, or incorporating additional data.
* Expanding to other countries: YOLOv5 has primarily been trained on datasets from Canada, North America and India, so there is a need to expand its capabilities to other regions around the world. Researchers could work on creating new datasets that include driving licenses from other countries and regions and then train the YOLOv5 model on this data to improve its performance in those areas.
* Extracting additional data fields: While YOLOv5 can currently extract data fields such as name, address, and date of birth, there may be other fields on driving licenses that could be useful to extract as well. For example, some countries include information about organ donor status or blood type on their licenses. Researchers could work on extending the YOLOv5 model to extract these additional data fields.
* Integrating with other systems: Once data is extracted from driving licenses, it needs to be integrated into other systems to be useful. Researchers could work on developing tools that allow the YOLOv5 model to seamlessly integrate with others. software systems, such as identity verification platforms, traffic management systems, or law enforcement databases.
Overall, there are many exciting possibilities for future work in driving license data extraction using the YOLOv5 model. As technology continues to evolve, we will likely see new and innovative approaches emerge to improve the accuracy and usefulness of this technology.


### Conclusion

In conclusion, the YOLOv5 model has proven to be an effective tool for extracting data from driving license images. Its fast and accurate object detection capabilities make it well-suited to identifying and extracting key information fields such as name, address, and date of birth. We have received an accuracy of 74% by training the YOLO v5 model.
By automating the process of extracting data from driving licenses, the YOLOv5 model can help streamline various workflows, from employment and banking applications to law enforcement and traffic management. This technology has the potential to save time and reduce errors while also improving safety and security.
Still, if we want more accurate results, we can train the model in a large dataset. In that way, we can increase the accuracy of the model and get better results.


### References 
[1] Jocher, G., Chaurasia, A., & Qiu, J. (2023, January 1). YOLO by Ultralytics. GitHub. https://github.com/ultralytics/ultralytics 
[2] Jocher, G. (2020, August 21). ultralytics/yolov5. GitHub. https://github.com/ultralytics/yolov5 


[3] Solawetz, J., Jan 11, F., & Read    2023 10 M. (2023, January 11). What is YOLOv8? The Ultimate Guide. Roboflow Blog. https://blog.roboflow.com/whats-new-in-yolov8/
[4] US-Driver-License-data-extraction/DATASET at master · lucky-verma/US-Driver-License-data-extraction. (n.d.). GitHub. Retrieved April 6, 2023, from https://github.com/lucky-verma/US-Driver-License-data-extraction/tree/master/DATASET 
[5]Pytorch https://pytorch.org/hub/ultralytics_yolov5/#:~:text=YOLOv5%20%F0%9F%9A%80%20is%20a%20family,size 
[6] Anindya. (2022, April 8). Upload and display image in Flask Python. ThinkInfi. https://thinkinfi.com/upload-and-display-image-in-flask-python/ 




