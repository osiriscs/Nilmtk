import nilmtk
from nilmtk import *
from nilmtk import DataSet
from nilmtk.utils import print_dict
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline


redd = DataSet('C:/Users/osiri/Documents/Nilmtk_estadias/nilmtk/data/random.h5')

elec = redd.buildings[1].elec

print(elec)
plt.plot(elec[1].power_series_all_data())