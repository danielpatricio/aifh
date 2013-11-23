__author__ = 'jheaton'

import os
import sys

# Find the AIFH core files
aifh_dir = os.path.dirname(os.path.abspath(__file__))
aifh_dir = os.path.abspath(aifh_dir + os.sep + ".." + os.sep + "lib" + os.sep + "aifh")                           
sys.path.append(aifh_dir)

from normalize import Normalize


# find the Iris data set
irisFile = os.path.dirname(os.path.realpath(__file__))
irisFile = os.path.abspath(irisFile + "../../datasets/iris.csv")

print('Reading CSV file: ' + irisFile)

norm = Normalize()

result = norm.load_csv(irisFile)
for i in range(0, 4):
    norm.make_numeric(result, i)
    norm.norm_range(result, i, -1, 1)

classes = norm.build_class_map(result, 4)
norm.norm_one_of_n(result, 4, classes)
norm.display_data(result)

print(classes)

