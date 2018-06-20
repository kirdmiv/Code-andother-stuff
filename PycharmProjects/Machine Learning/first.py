import numpy as np
from pandas import read_csv as read

PATH = "./wine.csv"
data = read(PATH, delimiter=",")
data.head()
