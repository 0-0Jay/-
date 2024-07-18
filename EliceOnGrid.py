# 엘리스 코드 챌린지 9번 - 격자 위의 ELICE
# ELICE를 순서대로 먹는 최단 경로 찾기

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
dt = [(0, 1), (1, 0)]
miro = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = tuple(map(int, input().split()))
    for j in range(1, n + 1):
        miro[i][j] = tmp[j - 1]
    
graph = [[] for _ in range(n * n + 1)]
que = deque([(1, 1)])
chk = set()
while que:
    x, y = que.popleft()
    node = (x - 1) * n + y
    if (x, y) in chk: continue
    chk.add((x, y))
    for dx, dy in dt:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            next_node = (nx - 1) * n + ny
            val = miro[x][y] + miro[nx][ny]
            graph[node].append((next_node, val))
            graph[next_node].append((node, val))
            que.append((nx, ny))

route = [[1]]
for i in "ELICE":
    a, b = map(int, input().split())
    node = (a - 1) * n + b
    route[0].append(node)
route2 = route[0][:]
route2[1], route2[-1] = route2[-1], route2[1]
route.append(route2)

def dijkstra(start, end):
    global graph, n, elice
    cost = [1e12] * (n * n + 1)
    heap = [(0, start)]
    cost[start] = 0

    while heap:
        co, now = hq.heappop(heap)
        if cost[now] < co: continue
        for nx, nco in graph[now]:
            if cost[nx] <= cost[now] + nco: continue
            cost[nx] = cost[now] + nco
            hq.heappush(heap, (cost[now], nx))
    return cost[end]

min_cnt = 1e12
for i in range(2):
    cnt = 0
    for j in range(1, 6):
        cnt += dijkstra(route[i][j - 1], route[i][j])
    min_cnt = min(cnt, min_cnt)

print(min_cnt)
        
# 알고리즘 : 다익스트라
'''
풀이 : 'ELICE'를 순서대로 먹어 완성할 수 있는 경우의 수는 2개이므로, 두 E에서 부터 다익스트라로 탐색한다.
맨처음 주어지는 격자의 각 지점에 대한 정보를 받고, 이를 정점간 간선 정보로 가공햐여 인접리스트로 만든다.(graph)
이 때, BFS를 응용하여 1,1에서 n,n까지 우측과 아래로만 퍼져나가게 하면서 양방향 간선을 모두 graph에 입력한다.
노드는 좌표로 계산하면 복잡하기 때문에 (x,y)로 이루어진 각 정점은 (x - 1) * n + y 공식으로 정점 번호로 바꾸어 저장한다.

다음으로 ELICE의 각 글자를 입력받는다.
입력받을 때, 그 좌표를 마찬가지로 (x - 1) * n + y 공식으로 정점번호로 바꾼뒤, 순서대로 route[0]에 저장한다.
이 route[0]에서 첫 E와 마지막 E의 좌표만 교환한 경로(route2)를 route[1]에 저장한다.

마지막으로 route의 0번에 저장된 루트와 1번에 저장된 루트 각각을 정점간 다익스트라로 최단 거리를 찾는다.
즉, 각 루트 별로 (E -> L)의 최단거리 + (L -> I)의 최단거리 ... (C -> E)의 최단거리를 계산하여 둘중 최소값을 출력한다.
'''
