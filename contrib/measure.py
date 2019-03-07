import implib2

bus = implib2.Bus('/dev/ttyUSB0')
bus.sync() # this command opens the port

# Notes: For SONO, just set the mode to C -> CS
# and then get_measurements()
#
# The "get_moisture()" command is a PICO specific call that includes
# a defined workflow
#


mod0 = implib2.Module(bus, 37552)

print mod0.get_event_mode()
mod0.set_event_mode()
if mod0.get_average_mode() is not "CS":
    mod0.set_average_mode("CS")
    print mod0.get_average_mode()

print 'Serno:' + str(mod0.get_serno())
print 'TransitTime: ' + str(mod0.get_measurement('TransitTime'))
print 'PseudoTransitTime: ' + str(mod0.get_measurement('PseudoTransitTime'))
print 'Moist: ' + str(mod0.get_measurement('Moist'))
print 'TDRValue: ' + str(mod0.get_measurement('TDRValue'))
print 'EC-TRIME: ' + str(mod0.get_measurement('Info1'))
print 'MeasTemp: ' + str(mod0.get_measurement('MeasTemp'))

print mod0.get_event_mode()

"""
mod0.set_event_mode("TDRScan")
data0 = bus.get_tdr_scan(37552, 0, 49, 1, 1024)
data1 = bus.get_tdr_scan(37552, 50, 99, 1, 1024)
data2 = bus.get_tdr_scan(37552, 100, 127, 1, 1024)
print data0
print data1
print data2
#print data

mod0.set_event_mode()
"""

import smbus
import time

bus = smbus.SMBus(1)

bus.write_i2c_block_data(0x44, 0x24, [0x00])

time.sleep(0.5)

data = bus.read_i2c_block_data(0x44, 0x00, 6)

print data

temp = data[0] * 256 + data[1]
cTemp = -45 + (175 * temp / 65535.0)
fTemp = -49 + (315 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

print "Temperature in Celsius is : %.2f C" %cTemp
print "Temperature in Fahrenheit is : %.2f F" %fTemp
print "Relative Humidity is : %.2f %%RH" %humidity


#print 'GetData: ' + str(mod0.get_measurement('GetData'))
#print mod0.get_moisture() # this command only works with PICO
