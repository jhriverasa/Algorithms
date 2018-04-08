import itertools
import sys
import math
def sumlist(Array,num,exp):  #0 nope #1 yep
	totsum = 0
	for i in range(len(Array)):
		totsum+= pow(Array[len(Array)-i-1] , exp)
		if(totsum>num):return 0
	if(totsum< num):
		return 0
	else:
		return 1

def isinlist(Array,thing): #0 nope #1 yep
	for i in range(len(Array)):
		if(Array[i] == thing):return 1
	return 0


def powerSum(X,N):
	#maxint ^ N <= 1000
	maxint =0
	l=[]
	counter=0
	while(pow(maxint+1,N)<=X):
		
		maxint+=1
		l.append(maxint)

	#heres list l is ready
	antirepeat=[]
	
	for j in range(maxint):
		index =0
		last=l[maxint-j-1]
		totalsum=pow(last,N)

		#add to list numbers to compute combinations
		lcomb=[]
		

		while(index<len(l) and totalsum + pow(l[index], N) <= X and  l[index]!=last):
			lcomb.append(l[index])
			index+=1
		lcomb.append(last)
		

		#create all combinations
		for k in range(len(lcomb)):
			combs = list(itertools.combinations(lcomb,k+1))
			for combindex in range(len(combs)):
				if(sumlist(combs[combindex], X, N) == 1 ):
					if(isinlist(antirepeat,combs[combindex]) == 0):
						antirepeat.append( combs[combindex] )
						counter+=1
						print combs[combindex]
		l.remove(last)
	return counter



#-------Main--------------
X= int(raw_input().strip())
N= int(raw_input().strip())
result = powerSum(X,N)
print result