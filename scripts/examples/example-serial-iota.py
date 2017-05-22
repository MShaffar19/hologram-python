#
# example-serial-iota.py - Example of using serial mode on the iota modem.
#
# Author: Hologram <support@hologram.io>
#
# Copyright 2016 - Hologram (Konekt, Inc.)
#
# LICENSE: Distributed under the terms of the MIT License
#

import sys

sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

from Hologram.HologramCloud import HologramCloud

if __name__ == "__main__":
    print ""
    print ""
    print "Testing Hologram Cloud class..."
    print ""
    print "* Note: You can obtain device keys from the Devices page"
    print "* at https://dashboard.hologram.io"
    print ""

    device_key = raw_input("What is your device key? ")

    credentials = {'devicekey': device_key}

    hologram = HologramCloud(credentials, enable_inbound = False, network='cellular-iota')

    print 'Signal strength: ' + hologram.network.signal_strength
    print 'IMSI: ' + hologram.network.imsi
    print 'ICCID: ' + hologram.network.iccid
    print 'Operator: ' + hologram.network.operator
    print 'Modem name: ' + hologram.network.active_modem_interface

    location = hologram.network.location
    print 'Latitude: ' + location.latitude
    print 'Longitude: ' + location.longitude
