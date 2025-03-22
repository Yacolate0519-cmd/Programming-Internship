#Progress Bar

from time import sleep
from tqdm import trange
x = 100
for i in trange(x):
    for j in range(x):
        k = i * j
        sleep(0.0002)
print('\n完成')