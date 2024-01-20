import cv2 
import pytesseract

# Adding custom options
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

custom_config=r'--psm 11 --oem 3 --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
# custom_config= r'--oem 3 --psm 11'

# custom_config =r'--psm 6 --oem 3'

def runOCR(img,x1,y1,x2,y2,cname):
    try :
        roi=img[y1:y2,x1:x2]
        output=pytesseract.image_to_string(roi,config=custom_config)
        return output
    except Exception as e:
        print(e)