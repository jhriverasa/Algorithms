
import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    r="NO"
    if(v1==v2):
        if(x1==x2):
            r = "YES"
    else:
        n=(x1-x2)/(v2-v1)
        nf = (x1-x2)/float((v2-v1))
        if(n>0 and n-nf==0):
            r= "YES"
    return r

        
        

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
