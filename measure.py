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

print 'Serno:' + str(mod0.get_serno())
print 'TransitTime: ' + str(mod0.get_measurement('TransitTime'))
print 'PseudoTransitTime: ' + str(mod0.get_measurement('PseudoTransitTime'))
print 'Moist: ' + str(mod0.get_measurement('Moist'))
print 'TDRValue: ' + str(mod0.get_measurement('TDRValue'))
print 'EC-TRIME: ' + str(mod0.get_measurement('Info1'))
print 'MeasTemp: ' + str(mod0.get_measurement('MeasTemp'))

print mod0.get_event_mode()

mod0.set_event_mode("TDRScan")
data = bus.get_tdr_scan(37552, 0, 49, 1, 1024)


print data

mod0.set_event_mode()


#print 'GetData: ' + str(mod0.get_measurement('GetData'))
#print mod0.get_moisture() # this command only works with PICO
