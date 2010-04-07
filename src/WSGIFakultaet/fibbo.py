import sys

# fn = fn-1 + fn-2 fuer n > 1
def fibbo(x):
    if x < 1:
        return 0
    if x == 1:
        return 1    

    return fibbo(x-1) + fibbo(x-2)


def main():
    if len(sys.argv)==2:
        x = int(sys.argv[1])
        y = fibbo(x)
        print y
        sys.exit()

if __name__=="__main__":
    main()
