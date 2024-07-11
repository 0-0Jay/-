# 엘리스 코드 챌린지 4번 - 트리 위의 게임
# 각자 최적 선택을 하는 경우, 승 패 결정하기

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
chk = set()
score = [0 for _ in range(n + 1)]
def DFS(now):
    global tree, chk, score
    chk.add(now)
    a, b, a_tmp, b_tmp = 0, 0, 0, 1e9
    for nx in tree[now]:
        if nx not in chk:
            a, b = DFS(nx)
            if a + now >= b:
                score[now] = 1
            if b - (a + now) < b_tmp - a_tmp:
                a_tmp, b_tmp = a + now, b
    chk.remove(now)
    if a == b == 0:
        score[now] = 1
        return 0, now
        
    return b_tmp, a_tmp
DFS(1)

for i in range(1, n + 1):
    print(score[i])

# 알고리즘 : 후위 DFS
'''
풀이 : 후위 재귀를 이용한 DFS를 통해 리프노드까지 내려간 후, 반환되는 점수들을 비교한다.
한 노드에서의 계산 과정은 다음과 같다.
1. 현재노드가 리프노드가 아니면, 자식 노드로 부터 상대에게 최악의 점수가 되는 경우를 받아온다.
2. 만약 자식으로 부터 반환된 점수에 현재 노드의 점수를 더했을 때, 점수가 더 높다면 현재 노드에서는 최적 선택의 경우에 승리할 수 있으므로 score[now]에 체크해둔다.
3. 모든 자식으로부터 반환된 점수에 대해 최악의 점수를 고른다.
 - 이 때 상대에게 최악의 점수가 되려면 자식이 반환한 점수들 중 내가 더 높은 점수를 얻으면서, 나와 상대가 얻을 수 있는 점수차가 클수록 유리하다.
4. 부모 노드로 다시 반환할 때는, 현재 노드의 점수는 상대편의 점수기 때문에 a와 b의 점수를 뒤집어 반환한다.
 - 만약 현재 노드가 리프노드라면, 자식 노드가 없기떄문에 내 점수(now)와 상대점수 0을 뒤집어 반환한다.

모든 노드의 계산이 끝나면 score에는 각 노드에서 시작했을 때 최적의 경우 승리할 수 있는지 여부가 기록되어 있다.
반복문을 통해 score를 출력해준다.
'''

