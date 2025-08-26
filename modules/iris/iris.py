import csv
import numpy as np


def iris():
    filename = 'files/pima-indians-diabetes.csv'
    raw_data = open(filename, 'r')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    x = list(reader)
    data = np.array(x).astype('float')
    print(data)
