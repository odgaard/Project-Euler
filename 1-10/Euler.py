def main():
	x=1.
	while x<1000:
		Euler = ((1.+(1./x))^x)
		if x%10000==0:
			print (Euler)
main()