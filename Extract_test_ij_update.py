# Created by Euan-Angus MacLeod
#
#Description: This code attempts to extract the lat, lon and the corresponding indices that store the environmental data
#input: tos_Omon_CNRM-CM5_historical_r1i1p1_197001-197912.nc
#output: SST_SP.csv
######################################


import netCDF4 
import numpy as np
import math
import csv
import os
import datetime 
from datetime import date

from netCDF4 import Dataset

os.chdir("C:\\Users\\Euan-Angus MacLeod\\Google Drive\\CSCE690_ Coastal Project\\Scripts")

file = "C:\\Users\\Euan-Angus MacLeod\\Google Drive\\CSCE690_ Coastal Project\\Data\\SST\\Historical\\CNRM_hist\\CNRM_hist\\tos_Omon_CNRM-CM5_historical_r1i1p1_197001-197912.nc"

nc = Dataset(file,'r')

tos = nc.variables['tos']
lat = nc.variables['lat']
lon = nc.variables['lon']
time = nc.variables['time']

print tos
print lat
print lon
print time

#Drew Point - Units: Decimal Degrees
DP_lat = 70.879
DP_lon = (360 - 153.932) #-153.932



##test for index / lat/lon - Identifies the points closest to the site
#CNRM_pnts = np.empty([1,4])

tol = 1 #search tolerance

closest_dist = 10000000000000000000000
closest_i = 1000
closest_j = 1000

print 'Calculating closest model point to Drew Point... \n'
for i in range(len(lat)):
    for j in range(len(lon)):
        if lat[i][j] > (DP_lat - tol) and lat[i][j] < (DP_lat + tol):
            if lon[i][j] > (DP_lon - tol) and lon[i][j] < (DP_lon + tol):
                dist_DP = math.sqrt((DP_lon - lon[i][j])**2 + (DP_lat - lat[i][j])**2) 
                
                if dist_DP < closest_dist:
                    closest_dist = dist_DP
                    closest_i = i
                    closest_j = j
                
                #print 'Lat:', lat[i][j], 'Lon:', lon[i][j], 'i:', i, 'j:', j
                
                #CNRM_pnts_row = np.array([lat[i][j],lon[i][j], i, j])
                
                #CNRM_pnts = np.vstack((CNRM_pnts, CNRM_pnts_row))
                
                #stack the each line of results to the empty array above 
#CNRM_pnts = np.delete(CNRM_pnts, (0), 0)
#print ' '
#print 'CNRM_pnts:'
#print CNRM_pnts
print 'Closest model point to Drew Point:'
print 'Lat:', lat[closest_i][closest_j], 'Lon:', lon[closest_i][closest_j], 'i:', closest_i, 'j:', closest_j


## Extract data from model for the appropriate time series

#work out the time variable
#extract the data for the location and the appropriate time
#the time variable is days from 1860-1-1
#store the data in CSV


## Worked with other model/GCM Variable - disregard at theis point in time


# Extract the temp data

#strt_date = time.index(1979-01-01)


tos_DP_ts = tos[:, closest_i, closest_j]


    
##
with open('tos.csv', 'w') as tempfile:
    wr = csv.writer(tempfile)
    wr.writerows(tslsi[2900, near_DP_lat, near_DP_lon])
