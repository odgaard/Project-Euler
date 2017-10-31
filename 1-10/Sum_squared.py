__author__ = 'Jacob'
def main():
    result1=0
    result2=0
    for x in range(0,101):
        result1 = (x**2)+result1
    print (result1)
    for x in range(0,101):
        result2 = x+result2
    print(result2**2)
    print((result2**2)-result1)
main()