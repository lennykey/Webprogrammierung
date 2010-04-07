import sys
import math

# fn = fn-1 + fn-2 fuer n > 1
def fibboRecursive(x):
    if x < 1:
        return 0
    if x == 1:
        return 1    

    return fibboRecursive(x-1) + fibboRecursive(x-2)

def fibboBinet(x):
    #(1 + math.sqrt(5)/2), 5
    binet = (1.0/math.sqrt(5.0)) * (pow(((1.0 + math.sqrt(5.0))/2.0), x) - pow(((1.0 - math.sqrt(5.0))/2.0), x))
    print binet
    return binet


def main():
    if len(sys.argv)==2:
        x = int(sys.argv[1])
        y = fibboRecursive(x)
        print y
        sys.exit()

if __name__=="__main__":
    main()
