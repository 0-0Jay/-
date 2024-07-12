# 엘리스 코드 챌린지 5번 - 수열 복원
# DFS로 조합 찾기

n = int(input())
arr = sorted(list(map(int, input().split())))
chk = {}
for i in arr:
    if i not in chk: chk[i] = 0
    chk[i] += 1
chk2 = [0]
res = []

def DFS(d):
    global n, arr, res
    if sorted(chk2) == arr:
        print(*res)
        exit(0)
    if len(res) == n: return
    for i in range(d + 1, len(arr)):
        if check(arr[i]):
            res.append(arr[i])
            DFS(i)
            res.pop()

def check(d):
    global chk, chk2
    tmp = {}
    for i in chk2:
        if d + i in chk:
            if d + i not in tmp: tmp[d + i] = 0
            tmp[d + i] += 1
            if chk[d + i] < tmp[d + i]: return False
        else: return False
    for k, v in tmp.items(): 
        chk[k] -= v
        chk2 += [k] * v
    return True

DFS(0)
print(*res)

# 알고리즘 : DFS + 딕셔너리
'''
풀이 : 수를 하나씩 선택해서 가능한 모든 부분 수열의 합을 구해 배열에 저장하고, 최종 배열과 비교한다.
제일 먼저 입력값을 저장할 배열(arr)과 각 값이 몇개씩 있는지를 체크해줄 딕셔너리(chk)를 생성한다.
이 때, arr은 오름차순 정렬을 하는 것이 탐색에 좋다.
왜냐하면 작은 값부터 탐색해야 작은 부분수열의 합부터 쌓이기 때문에 불필요한 중복 탐색을 방지할 수 있다.
이 후, 최종 값을 저장할 res 배열과 arr와 비교에 사용할 chk2 배열을 만들어 둔다.

숫자를 고르는 것은 DFS를 활용한다.
arr의 가장 작은 수부터 시작해서 n개를 고른다.
수를 하나 선택할 때마다 check함수를 통해 그 수를 선택했을 때 만들어지는 모든 부분수열 합값을 계산한다.
만약 만들어지는 부분수열 합들이 처음 주어진 arr에 속해있지 않거나, 속해있는 개수가 다르다면 숫자를 잘못 선택한 것이다.

check 함수의 계산 과정은 다음과 같다.
예를 들어 1을 선택했다고 하자. chk2에는 아무것도 선택하지 않았을 때의 부분합인 0이 기본값으로 들어있다.
chk2에는 지금까지 만들어 질 수 있는 부분합이 있으므로 chk2의 모든 수에 1을 더한 값 또한 새로운 부분합이 될 수 있다.
따라서 1을 선택했을 경우 chk2는 [0, 1]이 된다.
2를 선택했다면 [0, 1, 0 + 2, 1 + 2] => [0, 1, 2, 3]
3을 선택했다면 [0, 1, 2, 3, 0 + 3, 1 + 3, 2 + 3, 3 + 3] => {0, 1, 2, 3, 3, 4, 5, 6]
   :
입력 예제와 같이 [0, 1, 2, 3, 4, 5, 6, 7]인 경우, [1, 2, 3]을 선택했을 때의 부분합 배열과 다르기 때문에 정답 수열이 아닌 것이다.
check 함수에서 False가 반환되었다면 res에서 고른 숫자를 제거하고, arr에서 다음 숫자를 뽑아 추가해 check 함수로 확인하는 과정을 반복한다.

최종적으로 chk2와 arr의 원소가 같아지면 res에 저장된 뽑은 숫자들을 나열하고 exit를 통해 더이상 탐색하지 않게 프로그램을 종료시킨다.
'''
