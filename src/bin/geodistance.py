#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators
import sys
import geopy
from geopy.distance import vincenty

@Configuration()
class GeoDistCommand(StreamingCommand):
    # source="Brisbane Ferries Monitoring API" | head 1 | eval a=41.49008, b=-71.312796, x=41.499498, y=-81.695391 | geodistance latA=a lngA=b latB=x lngB=y meters=distance
    meters = Option(
        require=True, validate=validators.Fieldname())

    latA = Option(
        require=True, validate=validators.Fieldname())

    lngA = Option(
        require=True, validate=validators.Fieldname())

    latB = Option(
        require=True, validate=validators.Fieldname())

    lngB = Option(
        require=True, validate=validators.Fieldname())

    def stream(self, records):
        self.logger.debug('GeoDistCommand: %s', self)  # logs command line
 

        for record in records:

            latA = record[self.latA]
            lngA = record[self.lngA]
            latB = record[self.latB]
            lngB = record[self.lngB]
 
            distance = vincenty((latA,lngA), (latB,lngB)).meters

            record[self.meters] = distance
            yield record

dispatch(GeoDistCommand, sys.argv, sys.stdin, sys.stdout, __name__)
