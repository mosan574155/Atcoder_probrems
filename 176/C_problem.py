N = int(input())
a = list(map(int, input().split()))
ans = 0
max = a[0]
for i in range(1,N):
    if max<a[i]:
        max = a[i]
    else:
        ans += abs(a[i]-max)
print(ans)



