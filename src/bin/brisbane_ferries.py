#!/usr/bin/env python
import os
import random
import sys
import urllib2
import json
import csv
import time
import datetime

from splunklib.modularinput import *


class BrisbaneFerriesModularInput(Script):

    def get_scheme(self):
        scheme = Scheme("Brisbane Ferries")

        scheme.description = "Streams the location of Brisbane ferries."
        scheme.use_external_validation = True
        scheme.use_single_instance = True

        interval_in_secs = Argument("interval_in_secs")
        interval_in_secs.title = "Poll Interval (secs)"
        interval_in_secs.data_type = Argument.data_type_number
        interval_in_secs.description = "The interval to poll in seconds"
        interval_in_secs.required_on_create = True
        scheme.add_argument(interval_in_secs)

        return scheme

    def validate_input(self, validation_definition):
        pass

    def stream_events(self, inputs, ew):

        app_name = "brisbane_ferries"
        stops_csv_path = os.path.join(
            os.environ["SPLUNK_HOME"], "etc", "apps", app_name, "lookups", "ferry_stops.csv")

        ferry_refs = []
        with open(stops_csv_path, "rb") as csvfile:
            stops_reader = csv.DictReader(csvfile)
            for row in stops_reader:
                reference = row['ferry_stop_ref']
                ferry_refs.append(reference)

        # Go through each input for this modular input
        for input_name, input_item in inputs.inputs.iteritems():

            interval_in_secs = float(input_item["interval_in_secs"])

            while True:

                for reference in ferry_refs:

                    url = "https://svc.brisbane.qld.gov.au/api/ferry/stop-monitor?monitoringRef=" + \
                        str(reference)
                    data = json.load(urllib2.urlopen(url))

                    ferries = data["Siri"]["ServiceDelivery"][
                        "StopMonitoringDelivery"]["MonitoredStopVisit"]

                    valid_until = data["Siri"]["ServiceDelivery"][
                        "StopMonitoringDelivery"]["ValidUntil"]

                    for f in ferries:
                        if f["MonitoredVehicleJourney"]["VehicleRef"] <> "":

                            rec_time = f["RecordedAtTime"]
                            f["ValidUntil"] = valid_until

                            event = Event()
                            event.stanza = input_name
                            event.source = "Brisbane Ferries Monitoring API"
                            event.time = datetime.datetime.strptime(rec_time, "%Y-%m-%dT%H:%M:%S").strftime('%s')
                            event.data = json.dumps(f)

                            ew.write_event(event)

                time.sleep(interval_in_secs)

if __name__ == "__main__":
    sys.exit(BrisbaneFerriesModularInput().run(sys.argv))
