T=int(raw_input())
N=[]
count=1
while count<=T:
    N.append(int(raw_input()))
    count=count+1
for i in N:
    total=sum([j for j in range(1, i) if j%3==0 or j%5==0])
    print total
            
