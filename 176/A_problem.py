n,x,t = map(int, input().split())
ans = 0
tmp = 0
while True:
    tmp +=x
    ans +=t
    if tmp  >=n:
        break
print(ans)