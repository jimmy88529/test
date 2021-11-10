# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:00:28 2020

@author: wut
"""

import numpy as np
import os

# C:\Users\wut\Desktop\Python\Python_v1\py_section1\data
# directory to data location
sys_root = os.path.dirname(os.path.realpath(__file__))
print(sys_root)
# os.chdir("\\Users\PDAL\PycharmProjects\local_raspi\data")
root = sys_root + "\\data\\"
os.chdir(root)
file_names = os.listdir(os.getcwd())
path = sys_root + "\\data\\"
data_array = np.zeros((5000, 3 * 10))
file_count = 0
for file_name in file_names:
    a = path + file_name
    filename = np.loadtxt(a, dtype=str)
    temp = filename[:, 2:5].astype("float")
    [m, n] = np.shape(temp)  # obtain the size of array
    data_array[0:5000, 0 + (file_count) * 3:3 + (file_count) * 3] = temp
    file_count = file_count + 1
