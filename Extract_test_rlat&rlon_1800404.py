# Created by Euan-Angus MacLeod
#
#Description: This code attempts to extract the lat, lon and the corresponding indices that store the environmental data
#input: tos_Omon_GFDL-CM3_historical_r1i1p1_197501-197912.nc
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

file = "C:\\Users\\Euan-Angus MacLeod\\Google Drive\\Data\\GCM Data\\Non-ESM\\Historical\\GFDL-CM3\\tos_Omon_GFDL-CM3_historical_r1i1p1_197501-197912.nc"

nc = Dataset(file,'r')

tos = nc.variables['tos']
lat = nc.variables['lat']
lon = nc.variables['lon']
time = nc.variables['time']

print tos
print lat
print lon
print time

## rlat?

for i in range(190,200):
    for j in range(lon.shape[1]):
        print 'Lat:', lat[i][j], 'Lon:', lon[i][j], 'rlat:', i, 'rlon:', j
        
        
## Find Model Data Location
#Drew Point - Units: Decimal Degrees
DP_lat = 70.879
DP_lon = (360 - 153.932) #-153.932

s_tol = 1 #search tolerance

closest_dist = 10000000000000000000000
closest_i = 1000
closest_j = 1000

#this is not quite workign yet
#the length of the lat variable is ot the same as the length of the index rlat - how do i find the length of the index?

print 'Calculating closest model point to Drew Point... \n'
for rlat in range(lat.shape[0]):
    for rlon in range(lon.shape[1]):
        if lat[rlat][rlon] > (DP_lat - s_tol) and lat[rlat][rlon] < (DP_lat + s_tol):
            print 'lat:', lat[rlat][rlon]
            if lon[rlat][rlon] > (DP_lon - s_tol) and lon[rlat][rlon] < (DP_lon + s_tol):
                print 'lon: ',  lon[rlat][rlon]
                #dist_DP = math.sqrt((DP_lon - lon[rlat][rlon])**2 + (DP_lat - lat[rlat][rlon])**2) 
                
                #if dist_DP < closest_dist:
                    #closest_dist = dist_DP
                    #closest_i = i
                   # closest_j = j
                    
                #print 'Lat:', lat[rlat][rlon], 'Lon:', lon[rlat][rlon], 'rlat:', rlat, 'rlon:', rlon
                
                #model_pnts_row = np.array([lat[rlat][rlon],lon[rlat][rlon], rlat, rlon])
                
                #model_pnts = np.vstack((model_pnts, model_pnts_row))
                
                #stack the each line of results to the empty array above 
#model_pnts = np.delete(model_pnts, (0), 0)
#print ' '
#print 'model_pnts:'
#print model_pnts

#print 'Closest model point to Drew Point:'
#print 'Lat:', lat[closest_i][closest_j], 'Lon:', lon[closest_i][closest_j], 'i:', closest_i, 'j:', closest_j


## Extract the uas data

#strt_date = time.index(1979-01-01)
#current problem with the time: the count is days since 1860-01-01 00:00:00 in 0.125 increments (3hrs)

uas_DP_ts = uas[:, near_DP_lat, near_DP_lon]


## Write the lat/lon to file

with open('Lat.csv', 'w') as latfile:
    wr = csv.writer(latfile)
    wr.writerow(lat[:])

    
with open('Lon.csv', 'w') as lonfile:
    wr = csv.writer(lonfile)
    wr.writerows(lon[:])
    
##
with open('tslsi.csv', 'w') as tempfile:
    wr = csv.writer(tempfile)
    wr.writerows(tslsi[2900, near_DP_lat, near_DP_lon])
