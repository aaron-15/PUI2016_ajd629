
from __future__ import print_function
import sys
import pylab as pl
import json
import urllib as ulr
import os
import csv

apikey = sys.argv[1]
bus = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus) 

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


total_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

f = open(sys.argv[3], 'wb')
writer = csv.writer(f, delimiter=',')
writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

for i in range(len(total_data)):
    
    longitude = total_data[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = total_data[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
    if (total_data[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}):
        Location = 'N/A'
        StopPointName = 'N/A'
    
    else:        
        Location = total_data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
        ['Distances']['PresentableDistance']
        StopPointName = total_data[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    
    writer.writerow([latitude,longitude,Location,StopPointName])	


