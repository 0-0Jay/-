# 엘리스 코드 챌린지 1번 - 목표량
# 현재 수 보다 큰 수중 가장 작은 수 찾기

n = list(input())

min_num = '99'
for i in range(len(n)-2, -1, -1):
    if n[i] < n[i + 1]:
        idx = 0
        for j in range(i + 1, len(n)):
            if n[i] < n[j] and n[j] < min_num:
                min_num = n[j]
                idx = j
        n[i], n[idx] = n[idx], n[i]
        res = n[:i + 1] + sorted(n[i + 1:])
        print(''.join(res))
        break

# 알고리즘 : 그리디
'''
풀이 : 숫자의 1의 자리부터 순차적으로 검사하여 숫자가 감소하는 구간을 찾아 수를 교체한다.
1의 자리부터 순차적으로 검사하여 가장 처음 만나는 감소 구간을 찾는다.
왜냐하면 1의 자리부터 해당 자리까지의 숫자만 사용해서 더 큰 숫자를 만들 수 있기 때문이다.
예를 들어, 10의 자리보다 100의 자리 숫자가 작다면 100의 자리 숫자를 기준으로 잡는다.
그러면 1의 자리부터 100의 자리 숫자만 가지고 더 큰 숫자를 만들 수 있다.

교체할 i번째 숫자보다 크면서 i+1 부터 끝까지 숫자중 가장 작은 수를 찾아서 둘을 교체한다.
교체한 후에 i+1부터 끝까지의 숫자들을 오름차순 정렬한다.
이렇게 하면 현재 수보다 큰 수 중 가장 작은 수를 구할 수 있다.
'''
