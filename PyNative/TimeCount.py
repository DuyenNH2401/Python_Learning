import time
import math
start_time = time.time()


def exponent(base, exp):
    if exp <=0:
        return 1
    else: return base * exponent(base, exp-1)
exponent(123, 100)




end_time = time.time()
elapsed =end_time - start_time

print(elapsed)