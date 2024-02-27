import check_in
import pycron
import time
while True:
#                     |----------------- on minute 40
#                     |  |--------------- on hours 9 till 17:40
#                     |  |   | |-------- every day in month and every month
#                     V  V   V V  v------ on weekdays Monday till Friday
    if pycron.is_now('40 9-17 * * mon-fri'):
        check_in.check_in()
        break
time.sleep(40)