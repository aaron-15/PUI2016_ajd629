from __future__ import print_function
import sys
import pylab as pl
import json
import urllib as ulr
import os

apikey = sys.argv[1] 
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus) 

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

totalData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

i = 0

print("Bus Line : B52 ")
print("The Number of Actve Buses: %d" %(len(totalData)))

for total in totalData:
    longitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print ("Bus %d is at latitude %f and at longitude %f" %(i,latitude,longitude))
    i += 1