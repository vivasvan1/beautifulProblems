
import argparse

def gcd(x,y):
    if x==0 and y==0:
        return 0
    elif x==0:
        return y
    elif y==0:
        return x
    else:
        return gcd(y,x%y)

def gcdmulti(args):
    args = list(args)
    x = gcd(args.pop(),args.pop())
    while len(args):
        x = gcd(x,args.pop())

    return x
    



parser = argparse.ArgumentParser(description="GCD of integers: ")
parser.add_argument('integers',metavar="N", type=int,nargs='+',
                      help='intergers seperated by space whose GCD is to be computed')

args = parser.parse_args()
gcdmulti(args)


