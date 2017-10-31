from math import sqrt, ceil

highestPrime=0
def prime(num):
	if 600851475143%num==0:
		isPrime = primeCheck(num)
		if isPrime:
			print("%d is prime" % num)

def primeCheck(num):
	if num%2 == 0:
		return False
	for i in range(3, ceil(sqrt(num))+1, 2):
		if num%i == 0:
			return False
	return True

def main():
	for i in range(1, 10000000):
		prime(i)
#if __name__ == '__main__':
main()
