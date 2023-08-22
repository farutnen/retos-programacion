import  datetime
import time

def random():
    return time.time_ns().microsecond % 101

for _ in range(0, 101):
    print(random())