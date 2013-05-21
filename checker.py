import wmi

w=wmi.WMI()

# list all processors' information
for processor in w.Win32_Processor():
  print "CPU: %s,%s" %(processor.DeviceID, processor.Name)

#list the total memory
totalMemSize=0
for memModule in w.Win32_PhysicalMemory():
  totalMemSize+=int(memModule.Capacity)

print "Memory: %s" %totalMemSize

