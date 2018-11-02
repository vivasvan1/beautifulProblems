t = int(input())

def find_peeks(l):
    peeks = []
    for i in range(0,len(l)):
        if (i==0) and (l[i]>l[i+1]):
            peeks.append(l[i])
        elif (i == len(l)) and (l[i-1] <l[i]):
            peeks.append(l[i])
        elif (l[i+1]<l[i] and l[i-1]<l[i]):
            peeks.append(l[i])

    return peeks

def sol(l,lhigh,rhigh,high,counter):
    if (lhigh == l[0]):
        peeks =find_peeks(l[0:l.index(lhigh)])
        high = max(peeks)
        lhigh = max(peeks[0:peeks.index(high)])
        rhigh = max(peeks[peeks.index(high)+1:len(peeks)])
        sol(l[0:l.index(lhigh)],lhigh,rhigh,high,counter+1)
    



for i in range(0,t):
    peeks = []
    n = int(input())
    l = list(map(lambda x:int(x),input().split(" ")))
    

    

