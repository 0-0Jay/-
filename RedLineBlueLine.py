import heapq as hq
from copy import deepcopy

n = int(input())
arr = list(map(int, input().split()))
que = [(0, [set({i}) for i in range(n)], 0)] # 빨간 간선 개수, 연결 정점 상태, 추가 횟수
min_red = 1e9

while que:
    red, graph, d = hq.heappop(que)
    if red > min_red: continue
    if d == n - 1:
        min_red = min(min_red, red)
        break
    if arr[d] == 1:
        max_cnt = 0
        a, b, = 0, 0
        for i in range(n):
            if not graph[i]: continue
            for j in range(i + 1, n):
                if not graph[j]: continue
                if j not in graph[i] and len(graph[i]) * len(graph[j]) > max_cnt:
                    max_cnt = len(graph[i]) * len(graph[j])
                    a, b = i, j
        graph[a] |= graph[b]
        graph[b].clear()
        hq.heappush(que, (red, graph, d + 1))
    else:       
        chk = set()
        for i in range(n):
            if not graph[i]: continue
            for j in range(i + 1, n):
                if not graph[j]: continue
                if j not in graph[i] and (len(graph[i]), len(graph[j])) not in chk and (len(graph[j]), len(graph[i])) not in chk:
                    tmp_red = len(graph[i]) * len(graph[j]) + red
                    if tmp_red >= min_red: continue
                    tmp = deepcopy(graph)
                    tmp[i] |= tmp[j]
                    tmp[j].clear()
                    chk.add((len(graph[i]), len(graph[j])))
                    hq.heappush(que, (tmp_red, tmp, d + 1))

print(min_red)

# 알고리즘 : 힙 + BFS
'''
풀이 : 파란 간선일 때는 가장 큰 두 그룹을 연결하고, 빨간 간선일 때는 가장 작은 그룹부터 que에 넣어 BFS를 수행한다.
이 코드는 76점으로 오류가 있는 코드다.
첫 줄에 적혀 있든 파란 간선의 경우는 가장 큰 두 그룹을 찾아 한 그룹으로 만들고, 빨간 간선의 경우는 가장 작은 그룹끼리 합치려고 했다.
그러나 때로는 가장 작은 그룹이 아닌, 그룹과 연결했을 때 최종적으로 빨간 간선이 더 적어지는 경우가 있다.
이 경우를 정확하게 예외처리하지 못했다.

<<< 아래는 공개된 정답 코드 >>>
n = int(input())
c = list(map(int,input().split()))

dp = dict()
dp[tuple([1] * n)] = 0
queue = [tuple([1] * n)]
queueIndex = 0
while len(queue) > queueIndex:
    v = queue[queueIndex]
    queueIndex += 1
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            u = []
            for k in range(len(v)):
                if k == j:
                    u[i] += v[k]
                else:
                    u.append(v[k])
            u = tuple(sorted(u))
            if u not in dp:
                dp[u] = dp[v] + v[i] * v[j] * (1 - c[n - len(v)])
                queue.append(u)
            else:
                dp[u] = min(dp[u], dp[v] + v[i] * v[j] * (1 - c[n - len(v)]))
print(dp[(n,)])
'''
