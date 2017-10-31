def main():
	result=0
	x=0
	while x<1000:
		if x%3==0:
			print (x)
			result=x+result
		elif x%5==0:
			print (x)
			result=x+result
		x+=1
	print(result)
main()