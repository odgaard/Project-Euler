import random
def bSearch(x, P, L, U):
	half = (((L + U) // 2) + U) // 2
	half=(L +U) //2
	l_index,u_index=L,U
	while True:
		if P[half]==x:return half
		if P[half +1]>x:
			u_index=half +1
		if P[half]<x:
			l_index = half
		if P[half +1]>x>P[half]:
			return half
		half=(l_index + u_index) // 2


"""
	while True:
	    print(half)
	    if P[half+1]>x:
		    lowindex=half+1
		elif P[half]<x:
            highindex = half
	    else:
	        return half
        half = (lowindex+highindex)//2
"""
randomList=(random.sample(range(1000),800))
randomList.sort()
print(randomList)
result=(bSearch(686, randomList, 0, len(randomList)))
print(result,randomList[result])
