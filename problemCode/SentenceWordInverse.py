x = list(input("Input String: "))

x = x [::-1]

j = 0

def reverseword(x):
    i = 0
    print(int)  
    while i !=int(len(x)/2):
        temp = x[i]
        x[i] = x[len(x)-1-i]
        x[len(x)-1-i] = temp
        i+=1
    return str(x)

    
    
print(reverseword(x))
    
