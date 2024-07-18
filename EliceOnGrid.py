# 엘리스 코드 챌린지 9번 - 격자 위의 ELICE
# ELICE를 순서대로 먹는 최단 경로 찾기

from collections import defaultdict
import heapq as hq

def dijkstra(start, end):
    global graph, n, elice
    cost = [1e12] * (n * n)
    heap = [(0, start)]
    cost[start] = 0

    while heap:
        c, node = hq.heappop(heap)
        if cost[node] < c: continue
        for tnode, tc in graph[node]:
            if cost[tnode] <= cost[node] + tc: continue
            cost[tnode] = cost[node] + tc
            hq.heappush(heap, (cost[tnode], tnode))
    return cost[end]


n = int(input())
g = [tuple(map(int, input().split())) for _ in range(n)]
graph = defaultdict(list)
dire = ((-1, 0), (1, 0), (0, -1), (0, 1))

e = "ELICE"
elice = [0]
for i in e:
    a, b = map(int, input().split())
    elice.append((a - 1) * n + (b - 1))
temp = elice[:]
temp[1], temp[-1] = temp[-1], temp[1]
arr = []


for i in range(n):
    for j in range(n):
        for a, b in dire:
            tx, ty = i + a, j + b
            if not (0 <= tx < n and 0 <= ty < n): continue
            arr.append((i * n + j, tx * n + ty, g[i][j] + g[tx][ty]))
for st, ed, c in arr:
    graph[st].append((ed, c))
a1, a2 = 0, 0
for i in range(1, len(elice)):
    a1 += dijkstra(elice[i - 1], elice[i])
for i in range(1, len(elice)):
    a2 += dijkstra(temp[i - 1], temp[i])
print(min(a1, a2))


# 알고리즘 : 다익스트라
'''
풀이 : 'ELICE'를 순서대로 먹어 완성할 수 있는 경우의 수는 2개이므로, 플로이드 워셜로 모든 정점에서 다른 모든 정점까지의 최단거리를 구해두고 탐색한다.
처음 입력되는 5개의 좌표 중, 첫 번째 E와 마지막 E는 같은 글자이기 때문에 첫 번째 E를 가장 먼저 먹는 경우와 마지막 E를 가장 먼저 먹는 경우만 계산하면 된다.
먼저 주어지는 각 정점 별 점수와 BFS를 활용하여 정점간 간선(가중치) 정보로 가공한다.
이 때, (x, y) 좌표로 이루어진 2차원 정점 정보를 1차원 정보로 바꾸어 저장한다.
이 후, 플로이드 워셜을 통해 한 정점에서 다른 정점을 가는 최소값을 모두 구해둔다.
첫 줄에 적은 2가지 경우별 총 가중치 합을 최소값 비교하여 더 작은 값을 출력한다.
다익스트라로도 풀어보고, 플로이드 워셜로도 풀어봤으나 둘다 모두 58점으로 통과하지 
'''
