from copy import deepcopy
import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt
#%matplotlib inline
#plt.rcParams['figure.figsize'] = (16, 9)
#plt.style.use('ggplot')

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("Users.xml")
root = tree.getroot()

# open a file for writing

User_data = open('user_data1.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(User_data)

count = 0
csvwriter.writerow(['Reputation', 'Views', 'UpVotes', 'DownVotes', 'Age'])
for i in root.findall('row'):
    if i.get('Age') is None:
        continue
    data = [i.get('Reputation'), i.get('Views'), i.get('UpVotes'), i.get('DownVotes'), i.get('Age')]
#     print data
    
    count = count + 1
    csvwriter.writerow(data)
User_data.close()


