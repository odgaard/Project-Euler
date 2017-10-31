__author__ = 'Jacob'
def numGen():
    y=999
    while True:
        for x in range(999,0,-1):
            numCompare(x*y)
        y-=1
def numCompare(result):
    if result[0]==result[5] and result[1]==result[4] and result[2]==result[3]:
        print (result)
numGen()

