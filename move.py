# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 00:43:05 2016

@author: rahul
"""
import os
included_extensions = ['bmp']
filelist = [fn[0:26] for fn in os.listdir('/media/aj/OS/Users/SURENDRA JAIN/Documents/AJ/Acads/VIII sem/EE 625/ComputerVision_Project/Training images/Manual classification 02/Oxidation/') if any([fn.endswith(ext) for ext in included_extensions])]
filelist = list(set(filelist))
print filelist
oldpath = '/media/aj/OS/Users/SURENDRA JAIN/Documents/AJ/Acads/VIII sem/EE 625/ComputerVision_Project/Training images/Manual classification 02/Oxidation/'
newpath = '/media/aj/OS/Users/SURENDRA JAIN/Documents/AJ/Acads/VIII sem/EE 625/ComputerVision_Project/Training images/Manual classification 02/svm_data_oxidation/c1/'
for fname in filelist:
    oldname = oldpath + fname + 'c1.bmp'
    newname = newpath + fname + 'c1.bmp'
    os.rename(oldname, newname)