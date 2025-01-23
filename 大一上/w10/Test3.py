import datetime
import time
def get_time():
    current_time = datetime.datetime.now().time()
    return current_time.strftime("%I : %M : %S %p")

for i in range(100):
    print(get_time())  
    time.sleep(1)