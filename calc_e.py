import math
from decimal import Decimal, getcontext
import sys
import datetime
from progress_bar import progress_bar

t0= datetime.datetime.now()

getcontext().prec = 1000
sys.set_int_max_str_digits(1000000)
#a=10
a=100000
e=0

progress_bar.create_bar()

for i in range(a):
    e=Decimal(f"{e}")+ Decimal("1")/Decimal(f"{math.factorial(i)}")
    progress_bar.update_bar(a,i+1)

print("")
print(e)
print(f"Time: {datetime.datetime.now()-t0}")