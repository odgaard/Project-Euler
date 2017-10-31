from math import sqrt, ceil
import time
"""
__author__ = 'Jacob'
primeList = [0]
i = 0
primes = 1
def primeCheck(num):
    if num % 2 == 0: return False
    for i in range(3, ceil(sqrt(num)) + 1, 2):
        if num % i == 0: return False
    return True
for num in range(1, 10000000):
    if primeCheck(num):
        primeList.append(num)
        i+=1
        if i==10001: print(primeList[i])
"""
n,primes=100000,[2,3,5]
time0=time.time()

def prime(num,primes):
    for i in primes:
        if num % i==0: return False
        if i>ceil(sqrt(num)): return True
for num in range(3,n,2):
    if prime(num,primes): primes.append(num)
print(primes,len(primes),time.time() - time0)

"""
def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))
time0=time.time()


import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
if get_primes_erat(10**7):
    print("Done",time.time() - time0)

time0=time.time()
def sundaram3(max_n):
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)
        if initial > half:
            return [2] + filter(None, numbers)

if sundaram3(10**7):
    print("Done",time.time()-time0)

semi_list=[4,6,9,10,14]
num,Check=0,1
while Check:
    for i in range(len(primes)):
        if primes[num] * primes[i]>10**8:
            Check=0
            break
        if primes[num] * primes[i] not in semi_list:
            print(primes[num] + primes[i])
            semi_list.append(primes[num] * primes[i])
    num+=1
print(len(semi_list))
"""
import numpy
from math import log

def count_nonzero_sorted(array, count):
    # We always assume the count is achievable
    if array.shape[0] == 1:
        return 0

    midpoint = len(array) // 2
    first_half = array[:midpoint]
    second_half = array[midpoint:]

    first_counts = numpy.count_nonzero(first_half)

    if first_counts >= count:
        return count_nonzero_sorted(first_half, count)

    return midpoint + count_nonzero_sorted(second_half, count-first_counts)

def main():
    n = 100000
    maximum = int(n * (log(n) + log(log(n))))
    maxidx = maximum//2
    sieve = numpy.ones(maxidx, dtype=bool) # 2, 3, 5, 7... might be prime

    j = 0
    for i in range(1, int(maxidx**0.5)+1):
        j += 4*i

        if sieve[i]:
            sieve[j::2*i + 1] = False

    # compress sieve
    where = count_nonzero_sorted(sieve, n)
    print(2 * where + 1)

t0=time.time()
main()
print(time.time()-t0)
"""
db=[]
with open("text.txt",'r') as f:
    for line in f.readlines():
        db.append(line.replace(";"," ").replace("\n"," ").split())
print(db)

for x in range(5):
    continue
    print(x)
"""