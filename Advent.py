# 엘리스 코드 챌린지 8번 - 강림제
# 가장 길게 인원을 유지할 수 있는 방법 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k, t = map(int, input().split())
time = [0] * (n + 2)

for _ in range(m):
    a, b = map(int, input().split())
    time[a] += 1
    time[b] += -1

time[-1] = 1e9
run = [0] * (k + 1)
dp = [[0 for _ in range(k + 1)] for _ in range(n + 2)]
for i in range(1, n + 2):
    time[i] += time[i - 1]
    need = t - time[i] if t - time[i] > 0 else 0
    if need > 0:
        for j in range(need, k + 1):
            maxlen = 0
            for v in range(j + 1):
                maxlen = max(dp[i - 1][v], maxlen)
            dp[i][j] = maxlen + 1
    else:
        for j in range(k, -1, -1):
            maxlen = 0
            for v in range(j + 1):
                maxlen = max(dp[i - 1][v] + run[j - v] + 1, maxlen)
            dp[i][j] = 0
            run[j] = maxlen
            
print(max(run) - 1)

# 알고리즘 : DP
'''
풀이 : DP를 이용해 구간 별로 가장 길게 유지할 수 있는 인원 수를 찾는다.
개인일정 상 정답은 맞지 못한채로 넘겼지만 시도했던 풀이는 다음과 같다.
스위핑을 응용하여 각 시간별로 신도들이 차지하고 있는 부분을 미리 구해둔다.(time)
time을 활용해서 각 시간별로 필요한 추가 인원을 구한다.(need)
이 때, 이미 인원이 t명만큼 있는 경우는 친구들이 들어갈 수 없기 때문에 need를 0으로 맞춰준다
need가 양수라면, 신도가 t명보다 작고, 친구가 얼마든지 들어갈 수 있다는 뜻이다.
따라서 이전 시간까지 투입한 친구 수에 따른 dp 정보를 이용해 need명 부터 k명이 모두 들어가는 경우까지 현재 시간에 +1 해준다. 
만약 이번 시간에 신도들이 들어와서 t명을 넘겨버린 경우, 기존 친구들이 모두 도망간다.
따라서 이전 도망 시점의 정보(run)와 이번 도망 시점의 정보(dp[i - 1])를 이용해 각 인원수 별로 가장 길게 유지한 정보를 run에 갱신해준다.
이 후, 기존 인원이 남긴 정보를 사용할 수 없기 때문에 현재 시간은 각 인원 수 별 정보를 모두 0으로 초기화한다.
마지막까지 이렇게 계산하여 가장 길게 유지한 정보(max(run))에서 편의를 위해 time 배열의 마지막에 추가했던 1e9에 대한 1을 빼준다.

<< 정답 코드 >>
input = __import__("sys").stdin.readline
n, m, l, t = map(int, input().split())
a = [0] * n
for _ in range(m):
    i, j = map(int, input().split())
    for k in range(i - 1, j - 1):
        a[k] += 1
d = [0] * -~l
c = [0] * -~t
for i in range(n):
    if a[i] >= t:
        while len(c) > 1 and not c[-1]:
            c.pop()
        for i in range(len(c) - 1):
            c[i + 1] += c[i]
        d = [
            max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) + 1
            for i in range(l + 1)
        ]
        c = [0] * -~t
    else:
        c[t - a[i]] += 1
while len(c) > 1 and not c[-1]:
    c.pop()
for i in range(len(c) - 1):
    c[i + 1] += c[i]
d = [max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) for i in range(l + 1)]
print(d[-1])
'''
