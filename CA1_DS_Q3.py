n,m=map(int,input().split())
a=[[0]*m]*n
mat=[]
y=[]
k=0
h=0
for i in range(0,n):
	x=input().split()
	a[i]=list(map(int,x))
	mat.extend(x)
sort_mat=mat.sort()
a1=a
a2=a    
size=len(set(mat))
while (k < size) and len(a2) != 0 and len(a1) != 0: #((len(a2) != 1) or (len(a1) != 1)):
	a1=[list(m) for m in zip(*a2)] 
	if a1 != []  and len(a2) != 1:
		a1_set=list(set(a1[0]))
		if  len(a1) == 1 and len(a1_set) != 1:
			h=99#it is extra nothing
		else:#
			i=0
			mat_column=[]
			while i < len(a1):# column
				check1=a1[i][0]
				if a1[i].count(check1)==len(a1[i]):
					mat_column.append(check1)
					a1.remove(a1[i]) 
				else:
					i=i+1
			mat_column.sort()
			y.extend(mat_column[::-1])	
	a2=[list(n) for n in zip(*a1)] 
	if a2 != [] and len(a1) != 1:
		a2_set=list(set(a2[0]))
		len_a2_set=len(a2_set)
		len_a2=len(a2)
		if  len_a2==1 and len_a2_set != len_a2:
			h=100 #it is exra nothing
		else:
			j=0
			mat_line=[]
			while j < len(a2):#line
				check2=a2[j][0]
				if a2[j].count(check2)==len(a2[j]):
					mat_line.append(check2)
					a2.remove(a2[j])
				else:
					j=j+1
			mat_line.sort()		
			y.extend(mat_line[::-1])
	k=k+1
if len(a2)==1:
	a2_set=list(set(a2[0]))
	if len(a2_set) != len(a2[0]):
		a2_set.sort()
		for i in a2_set:
			if a2[0].count(i) > 1:
				a2_set.remove(i)
				z=a2_set[::-1]
				z.append(i)
	else:
		z=a2_set[::-1]			
	y.extend(z)
if len(a1)==1:
	a1_set=list(set(a1[0]))
	if len(a1_set) != len(a1[0]):
		a1_set.sort()
		for i in a1_set:
			if a1[0].count(i) > 1:
				a1_set.remove(i)
				z=a1_set[::-1] 
				z.append(i)				
	else:
		z=a1_set[::-1]
	y.extend(z)	
y=y[::-1]
for i in y:
	print(i,end=' ')
