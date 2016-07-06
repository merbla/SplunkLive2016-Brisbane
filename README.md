# Splunk Live 2016 - Brisbane

Using data from the [Brisbane City Council OpenData](https://www.data.brisbane.qld.gov.au/data/dataset/ferry-terminals) this app illustrates some of the capabilites of Splunk apps using Open Data.

* [Lookup Data](http://docs.splunk.com/Documentation/Splunk/6.4.1/Knowledge/Addfieldsfromexternaldatasources)
* [Modular Inputs](http://docs.splunk.com/Documentation/Splunk/latest/AdvancedDev/ModInputsIntro) 
* [Location Tracker](http://docs.splunk.com/Documentation/CustomViz/1.0.0/RealTimeLocation/RealTimeTrackerIntro)
* [Custom Search Commands](http://docs.splunk.com/Documentation/Splunk/6.4.1/Search/Aboutcustomsearchcommands)

This app makes use of the following OSS libraries:

* [Splunk Python SDK](https://github.com/splunk/splunk-sdk-python)
* [GeoPy](https://github.com/geopy/geopy)

You will need the latest version of the [Location Tracker](http://docs.splunk.com/Documentation/CustomViz/1.0.0/RealTimeLocation/RealTimeTrackerIntro) installed on your Splunk instance.  You can get it from Splunkbase [here](https://splunkbase.splunk.com/app/3164/)