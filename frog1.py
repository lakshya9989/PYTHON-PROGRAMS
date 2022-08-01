def dp(i):
    cost=1000
    if i==0:
        return 0
    if i in dic:
        return dic[i]
    cost=min(cost,dp(i-1)+abs(l[i]-l[i-1]))
    if i>1:
        cost=min(cost,dp(i-2)+abs(l[i]-l[i-2]))
    dic[i]=cost
    return cost
dic={}
l=list(map(int,input('enter the stairs ').split()))
print(l)
n=len(l)
x=dp(n-1)
print(x)
