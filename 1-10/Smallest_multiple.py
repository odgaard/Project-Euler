import math
def main():
    x=0
    num=5
    primes = [1,2,3,5,7,11,13,17,19]
    counter=1
    while True:
        if not all(num% n ==0 for n in range(1,20)):
            num+=1
        elif all(num% n ==0 for n in range(1,20)):
            print (num)
main()

