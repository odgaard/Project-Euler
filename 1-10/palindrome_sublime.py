__author__ = 'Jacob'

def numGen():
	y=999
	global resultList
	resultList=[0,1]
	maxList=[0,1]
	while y>0:
		for x in range(999,0,-1):
			numCompare(x*y)
		y-=1
		maxList.append(max(resultList))
	print (max(maxList))
	inpit = input("sfsa")
def numCompare(result):
	result=str(result)
	if len(result)==6:
		if (result[0]==result[5]) and (result[1]==result[4]) and (result[2]==result[3]):
			resultList.append(int(result))
numGen()
