# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:50:44 2016

@author: michw
"""

import pandas as pd
import numpy as np
import xarray
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')  

ncfile = 'woa13_A5B2_t00_01v2.nc'
xdf = xarray.open_dataset(ncfile,decode_times=False)

justdata = xdf.t_an.data
dslice = justdata[0,0,:,:]

latcorners = xdf.variables['lat']
loncorners = xdf.variables['lon']