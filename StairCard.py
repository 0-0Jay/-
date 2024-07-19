# 엘리스 코드 챌린지 10번 - 계단 카드 뽑기
# 연속된 k개의 주머니를 고르고, 각 주머니에서 숫자를 하나씩 뽑아 1~k가 하나씩 포함되게 할 수 있는 가장 긴 k값 찾기

n = int(input())
arr = list(map(int, input().split()))

maxk = 0
left, right = 0, 0
chk = {}
while right < len(arr):
    if arr[right] not in chk: chk[arr[right]] = 0
    chk[arr[right]] += 1
    while chk[arr[right]] > arr[right]:
        chk[arr[left]] -= 1
        left += 1
    right += 1
    maxk = max(maxk, right - left)
        
print(maxk)

# 알고리즘 : 투 포인터
'''
풀이 : k의 길이에 따라 각 숫자별로 그 숫자보다 높은 숫자의 개수를 체크한다.
반례를 찾았지만 시간초과를 해결하지 못했다.
위 풀이는 다음과 같다.
right를 한칸씩 오른쪽으로 옮겨가며 주머니를 선택한다.
만약 선택한 주머니의 카드 수와 같은 주머니의 개수가 그 주머니의 카드 수보다 많다면, 1개씩 뽑아서 1~k가 하나씩 포함되게 할 수 없다.
-> (1 2 3) (1 2 3) (1 2 3) (1 2 3) 이라면, 4를 뽑을 수 있는 주머니가 없다.
따라서 해당 주머니 개수가 주머니의 카드 수보다 적어질 때까지 left를 한 칸씩 옮겨준다.
매 상황마다 maxk에 최대 길이를 계산한다.
'''
