import time
print "Enter an n:"
n= 30 #put your n
A=[[],[]]
B=[[],[]]
C=[[],[]]
mean =0

r=n
c=n
A=[1]*r
B=[1]*r
C=[1]*r
for i in range(r):
    A[i]=[1]*c
    B[i]=[2]*c
    C[i]=[1]*c
startTime = time.time()
for row in range(n):
    for col in range(n):
        result=0
        for m in range(n):
           
            result= result + A[row][m]*B[m][col]  
           

        C[row][col] = result
        #System.out.print(result + " ");
        #System.out.print("\n");

print "---------"
duration = (time.time() - startTime)
print (int(duration*1000000000))
