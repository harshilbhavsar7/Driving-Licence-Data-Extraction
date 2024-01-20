#! usr/bin/python
from datetime import datetime
import os

today = datetime.now()


def create_today_folder(folder):
    if today.hour < 12:
        h = "00"
    else:
        h = "12"

    path=folder+"/"+today.strftime('%Y%m%d')+ h

    if not os.path.exists(path):
        os.makedirs(path)
     
    return path 