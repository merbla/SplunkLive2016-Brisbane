




source="Brisbane Ferries Monitoring API" 
| spath output=Arrival path=MonitoredVehicleJourney.MonitoredCall.AimedArrivalTime
| spath output=ExpectedArrival path=MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime
| spath output=Destination path=MonitoredVehicleJourney.DestinationName
| eval at = strptime(Arrival, "%Y-%m-%dT%H:%M:%S.%3N")
| eval et = strptime(ExpectedArrival, "%Y-%m-%dT%H:%M:%S.%3N")
| eval diff = coalesce(at-et,0)/60
| timechart span=1m sum(diff) by Destination


source="Brisbane Ferries Monitoring API" 
| spath output=Arrival path=MonitoredVehicleJourney.MonitoredCall.AimedArrivalTime
| spath output=ExpectedArrival path=MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime
| spath output=Destination path=MonitoredVehicleJourney.DestinationName
| eval at = strptime(Arrival, "%Y-%m-%dT%H:%M:%S.%3N")
| eval et = strptime(ExpectedArrival, "%Y-%m-%dT%H:%M:%S.%3N")
| eval diff = at-et
| table at, Destination, diff




source="Brisbane Ferries Monitoring API" 
| spath output=VehicleRef path=MonitoredVehicleJourney.MonitoredCall.VehicleRef
| stats max(ValidUntil) by VehicleRef

hour=strftime(x,"%H")

VehicleRef

ValidUntil






 your_base_search 
 | eval it = strptime(in_time, "%Y-%m-%dT%H:%M:%S.%3N") 
 | eval ot = strptime(out_time, "%Y-%m-%dT%H:%M:%S.%3N") 
 | eval diff = tostring((ot - it), "duration") 
 | table in_time, out_time, diff 







source="Brisbane Ferries Monitoring API" 
| spath output=Arrival path=MonitoredVehicleJourney.MonitoredCall.AimedArrivalTime
| spath output=ExpectedArrival path=MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime
| spath output=Destination path=MonitoredVehicleJourney.DestinationName





source="Brisbane Ferries Monitoring API"  | spath "MonitoredVehicleJourney.DestinationName" | search "MonitoredVehicleJourney.DestinationName"="Riverside" | eval x=strptime(RecordedAtTime, "%Y-%m-%dT%H:%M:%S") 
| eval hour=strftime(x,"%H") | stats count(MonitoringRef),  by hour, MonitoredVehicleJourney.VehicleRef


source="Brisbane Ferries Monitoring API"  | where MonitoringRef="317590" | eval x=strptime(RecordedAtTime, "%Y-%m-%dT%H:%M:%S") 
| eval hour=strftime(x,"%H") | stats count(MonitoringRef),  by hour, MonitoredVehicleJourney.VehicleRef


spath output=commit_author path=commits.author.name


 | spath output=dest path=MonitoredVehicleJourney.DestinationName


| spath output=ExpectedArrival path=MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime
source="Brisbane Ferries Monitoring API" | spath output=ExpectedArrival path=MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime





convert timeformat="%H:%M:%S" ctime(_time) AS c_time


source="Brisbane Ferries Monitoring API"  | where MonitoringRef="317590" | eval x=strptime(RecordedAtTime, "%Y-%m-%dT%H:%M:%S")

source="Brisbane Ferries Monitoring API"  | where MonitoringRef="317590" convert timeformat= "%Y-%m-%dT%H:%M:%S" ctime(RecordedAtTime) AS c_time





source="Brisbane Ferries Monitoring API"  | where MonitoringRef="317590" | search "MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime"="2016-07-03T12:11:29" | eval n=strptime("12:50", "%H:%M") | eval expected=substr(MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime,11,5)


source="Brisbane Ferries Monitoring API" | where MonitoringRef="317590" |eval ot = strptime(MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime, "%Y-%m-%dT%H:%M:%S")




eval xxx = strptime(your_date_field,"%a, %d %b %Y %H:%M:%S %z")
eval a = 
strptime(MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime, "%Y-%m-%dT%H:%M:%S") |
eval b = strftime(a, '%s')



source="Brisbane Ferries Monitoring API" | where MonitoringRef="317590" | eval  RiverSideLat=-27.467087, RiverSideLong=153.031222  | table _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef, RiverSideLat, RiverSideLong |
geodistance latA=MonitoredVehicleJourney.VehicleLocation.Latitude lngA=MonitoredVehicleJourney.VehicleLocation.Longitude latB=RiverSideLat lngB=RiverSideLong meters=distance | where distance <1000 | sort distance


source="Brisbane Ferries Monitoring API" | where MonitoringRef="317590" | eval  RiverSideLat=-27.467087, RiverSideLong=153.031222  | table _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef, RiverSideLat, RiverSideLong, MonitoringRef |
geodistance latA=MonitoredVehicleJourney.VehicleLocation.Latitude lngA=MonitoredVehicleJourney.VehicleLocation.Longitude latB=RiverSideLat lngB=RiverSideLong meters=distance | where distance <1000


source="Brisbane Ferries Monitoring API" | where MonitoringRef="317590"
| eval RiverSideLat=-27.467087, RiverSideLong=153.031222 
| rename MonitoredVehicleJourney.VehicleLocation.Latitude AS FerryLat 
| rename MonitoredVehicleJourney.VehicleLocation.Longitude AS FerryLong
| geodistance latA=FerryLat lngA=FerryLong latB=RiverSideLat lngB=RiverSideLong meters=distance 
| where distance <100
| stats count by date_hour by MonitoringRef 



eval xxx = strptime(your_date_field,"%a, %d %b %Y %H:%M:%S %z")
eval a = 
strptime(MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime, "%Y-%m-%dT%H:%M:%S") |
eval b = strftime(a, '%s')



convert timeformat="%Y-%m-%dT%H:%M:%S" ctime(MonitoredVehicleJourney.MonitoredCall.ExpectedArrivalTime) AS c_time

source="Brisbane Ferries Monitoring API" | where MonitoringRef="317590"
| eval RiverSideLat=-27.467087, RiverSideLong=153.031222 
| rename MonitoredVehicleJourney.VehicleLocation.Latitude AS FerryLat 
| rename MonitoredVehicleJourney.VehicleLocation.Longitude AS FerryLong
| geodistance latA=FerryLat lngA=FerryLong latB=RiverSideLat lngB=RiverSideLong meters=distance 
| where distance <100
| stats count by date_hour by MonitoringRef



convert timeformat="%H:%M:%S" ctime(_time) AS c_time








<!-- 

source="Brisbane Ferries Monitoring API" | table _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef  | eval a=-27.463576, b=153.035603 | geodistance latA=a lngA=b latB=MonitoredVehicleJourney.VehicleLocation.Latitude lngB=MonitoredVehicleJourney.VehicleLocation.Longitude meters=distance | where distance <1000 | sort distance










  source="Brisbane Ferries Monitoring API" | table _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef  | eval a=-27.463576, b=153.035603 | geodistance latA=a lngA=b latB=MonitoredVehicleJourney.VehicleLocation.Latitude lngB=MonitoredVehicleJourney.VehicleLocation.Longitude meters=distance |sort _time |head 100

  source="Brisbane Ferries Monitoring API" | eval t=strftime(_time, "%H:%M:%S %m-%d-%y")| table _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef strftime(_time, "%H:%M:%S %m-%d-%y") | stats latest(_time) as stop by MonitoredVehicleJourney.VehicleRef


  # source="Brisbane Ferries Monitoring API" | head 1 | eval a=41.49008, b=-71.312796, x=41.499498, y=-81.695391 | geodistance latA=a lngA=b latB=x lngB=y meters=distance
source="Brisbane Ferries Monitoring API"  "MonitoredVehicleJourney.VehicleRef"=26624 | table  _time MonitoredVehicleJourney.VehicleLocation.Latitude MonitoredVehicleJourney.VehicleLocation.Longitude MonitoredVehicleJourney.VehicleRef | sort  -_time  |head 1 -->


<!-- 


a=-27.463576 b=153.035603



-27.463400

153.035581

http://geopy.readthedocs.io/en/latest/  


Latitude:-27.463576°
Longitude:153.035603°


-->