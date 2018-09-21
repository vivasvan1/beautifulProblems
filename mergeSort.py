def merge(X,Y):
    z = []
    while not((len(Y)==0) and (len(X)==0)):
        if len(X) ==0:
            z.append(Y.pop(0))
        elif len(Y) ==0:
            z.append(X.pop(0))
        else:
            if X[0]>=Y[0]:
                z.append(Y.pop(0))
            else:
                z.append(X.pop(0))
    return z

def mergeSort(A):
    if len(A)==1:
        return A
    first = 0
    last = len(A)
    mid = int((last-first)/2)
    return merge(mergeSort(A[first:mid]),mergeSort(A[mid:last]))

A = [8,4,3,7,6,1,2,5]
print(mergeSort(A))