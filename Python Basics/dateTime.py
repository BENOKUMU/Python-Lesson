import time
import calendar

ticks = time.time()
# print(ticks)
# print(time.localtime())

# localtime = time.localtime(time.time())
# print(localtime)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# cal= calendar.month(2016,2)
# print(cal)
# print(time.altzone)

# def procedure():
#     time.sleep(2.5)
    
# t0 = time.clock()
# procedure()
# print(time.clock() - t0)

# t0 = time.time()
# procedure()
# print(time.time())

print(time.ctime())
time.sleep(5)
print("End: %s" % time.ctime())

import os
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))