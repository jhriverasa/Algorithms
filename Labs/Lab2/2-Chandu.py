
from __future__ import print_function
t=int(raw_input())

for i in range(t):
	raw=raw_input().split()
	n=int(raw[0])
	m=int(raw[1])
	A = map(int,raw_input().split())
	B = map(int,raw_input().split())
	merged = []
	j=0
	k=0
	counter=0
	while(counter<n+m):
		if(A[j]>B[k]):
			merged.append(A[j])
			counter= counter +1
			j=j+1
			if(j==n):
				while(k<m):
					merged.append(B[k])
					counter= counter +1
					k=k+1
		else:
			merged.append(B[k])
			counter= counter +1
			k=k+1
			if(k==m):
				while(j<n):
					merged.append(A[j])
					counter= counter +1
					j=j+1

	for z in range(n+m):
	    print (merged[z], sep= ' ',end =' ')
	print("")