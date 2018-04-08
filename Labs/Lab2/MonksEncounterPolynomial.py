def binarySearch(A,B,C,K):
	first=0
	last = 50000
	found = False

	if(C >= K):return 0

	while (first<=last and not found):
		midpoint = (first + last )//2
		if (( A*pow(midpoint,2) ) + (B*midpoint) + C >= K) and ( (A*pow(midpoint-1,2) ) + (B*(midpoint-1)) + C < K ):
			found = True
		else:
			if (( A*pow(midpoint,2) ) + (B*midpoint) + C < K):
				first = midpoint-1
			else:
				last = midpoint+1

	return midpoint


T= int(raw_input())
for i in range(T):
	raw = map(int,raw_input().split())
	A = raw[0]
	B = raw[1]
	C = raw[2]
	K = raw[3]
	print binarySearch(A,B,C,K)



