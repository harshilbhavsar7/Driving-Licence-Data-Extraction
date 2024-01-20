# Importing essential libraries
from flask import Flask,render_template,request,redirect,url_for,send_from_directory,jsonify,flash
from werkzeug.utils import secure_filename
import os
import socket
import pandas as pd
from custom.create_today_folder import create_today_folder
from custom.storing import store_excel
from custom.global_data import class_names
import custom.initialize_run as initrun


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

api_input= './api_input'
folder=create_today_folder(api_input)
UPLOAD_FOLDER=folder
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


'''Get host IP address'''
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
initrun.init()
dictimages={}


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'files' not in request.files:
            print('Error accured')
            return redirect(request.url)
        files = request.files.getlist('files')
        print(files)
        for file in files:
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                folder=create_today_folder(api_input)
                UPLOAD_FOLDER=folder
                app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                try :
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    dictpred = initrun.run(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    dictimages[filename]= dictpred.copy()
                except Exception as e:
                    print(e)

        resp = jsonify(dictimages)
        print(resp)
        final_dict_df = pd.DataFrame.from_dict(dictimages,orient='index',columns=class_names)
        store_excel(final_dict_df)
        resp.status_code = 201
        dictimages.clear()
        # return resp

        return render_template('dle_result.html', column_names=final_dict_df.columns.values, row_data=list(final_dict_df.values.tolist()),
                           link_column="face", zip=zip)
    
    return render_template('dle_home.html', result = dictimages)

if __name__ == '__main__':
  # app.debug = True
  app.run(host='0.0.0.0', port=5000, debug=True)