#!/usr/bin/env python3

import os
import pandas as pd
from pandasql import sqldf

#Parts = xl.load_workbook('PC Part Spreadsheet.xlsx')
#dataframe = Parts.active

directory = '~/PC_Part_Picker/Parts/'
Parts = []

counter = 0
for filename in os.listdir(directory):
    Parts[counter] = pd.read_csv(filename)
    counter += 1
Parts[0].head(3)

"""
CPUs = pd.read_csv('PC Part Spreadsheet - CPUs.csv')
GPUs = pd.read_csv('PC Part Spreadsheet - GPUs.csv')
MoBos = pd.read_csv('PC Part Spreadsheet - MoBos.csv')
SSDs = pd.read_csv('PC Part Spreadsheet - SDDs.csv')
HDDs = pd.read_csv('PC Part Spreadsheet - HDDs.csv')
RAM = pd.read_csv('PC Part Spreadsheet - RAM.csv')
"""
#print(sqldf("SELECT * FROM Parts;"))
"""
dataframe = Parts.active

for row in range(0, dataframe.max_row):
    
Parts.head()

print(Parts)
"""



"""class Parts:
    pass
class Cpu:
    def __init__(self, use, price, performance, tdp, igpu, p_cores, e_cores, threads, OC, DDR4, DDR5, cooler):
        self.use = use
        self.price = price
        self.performance = performance
        self.tdp = tdp
        self.igpu = igpu
        self.p_cores = p_cores
        self.e_cores = e_cores
        self.threads = threads
        self.OC = OC
        self.DDR4 = DDR4
        self.DDR5 = DDR5
        self.cooler = cooler
class Gpu:
    def __init__(s):

class storage:
    pass

"""
"""
def __init__(self, cpu, gpu, storage, ram, case, psu):
        self.cpu = cpu
        self.gpu = gpu
        self.storage = storage
        self.ram = ram
        self.case = case
        self.psu = psu
    def __str__():
        

"""