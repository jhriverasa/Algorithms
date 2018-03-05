
import sys
#Create variables and assign their initial values.
IntFn_2=0
IntFn_1=1
IntFn=0
#try to compute 100-th term of fibonacci secuence .
n= 100
overFlow=0
for i in range(n):
    IntAux=IntFn 
    IntFn_2=IntFn_1
    IntFn_1=IntFn
    IntFn=IntFn_2+IntFn_1
    #--------   
    if(IntFn>sys.maxint and overFlow==0):
        print ("Overflow computing "+str(i)+"-th term of Fibonacci Sequence(data type: Int) ");
        overFlow=1
