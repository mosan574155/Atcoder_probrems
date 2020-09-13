S = str(input())
T = str(input())
ans = 1001
for i in range(len(S)-len(T)+1):
    S_t = S[i:i+len(T)]
    count = 0
    for j in range(len(T)):
        if S_t[j]!=T[j]:
            count +=1
    ans = min(count,ans)
print(ans)