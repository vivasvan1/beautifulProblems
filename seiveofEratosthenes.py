import argparse
import math


def sieve(b):
    nums = list(range(2,b+1))
    for p in range(2,int(math.ceil(math.sqrt(b)))):
        if nums[p-2] != 0:
            j = p*p
            while j<=b:
                nums[j-2] = 0
                j = j+p
    prime = []
    for num in nums:
        if num != 0:
            prime.append(num)
    print(len(prime))
    return 0

sieve(10000000)


    


# parser = argparse.ArgumentParser(description="To find the prime between 2 numbers")
# parser.add_argument('integers',metavar="N", type=int,nargs='+',
#                       help='intergers seperated by space whose inbetween prime are to be searched for')

# args = parser.parse_args()
# (args)