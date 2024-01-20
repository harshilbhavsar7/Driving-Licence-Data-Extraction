checkpoint_file = r"C:\Harshil\Study\Semester_2\AI_ML_Lab\Final_Project\Driving_Licence_Extract_API\model_checkpoints\model_final.pt"

#new class names
class_names= ['dob','exp_date','name','address','sex','issue_date','face','license_number']

# Storage
input_dir = './api_input'
output_dir = './api_output'

ocrdict={}

# Debugging
debugger_enable = False
