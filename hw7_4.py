# -*- coding: utf-8 -*-

import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d

path = raw_input("Введите путь к папке: ")
f_s=open("result_path.json", "wb")
json.dump(path_to_dict(path), f_s)
f_s.close()