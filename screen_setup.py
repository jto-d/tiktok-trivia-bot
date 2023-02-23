import pywinctl
import time

# RUN ONLY ON FIRST RUN
my = pywinctl.getWindowsWithTitle('Movie Recording')[0]
my.moveTo(0, 0)
time.sleep(0.1)
my.activate()
time.sleep(0.1)