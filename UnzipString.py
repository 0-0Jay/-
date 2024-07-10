# 엘리스 코드 챌린지 3번 - 문자열 압축 해제
# 괄호 안의 문자열 곱하기

arr = tuple(input())
stk = []

for i in range(len(arr)):
    if not stk or arr[i] != ')': stk.append(arr[i])
    elif arr[i] == ')':
        tmp = []
        while stk[-1] != '(':
            tmp.append(stk.pop())
        stk.pop()
        tmp *= int(stk.pop())
        while tmp:
            stk.append(tmp.pop())
print(len(stk))

# 알고리즘 : 스택
'''
풀이 : 스택을 활용해 문자열을 삽입하고, 닫는 괄호가 나올때마다 문자열을 계산한다.
스택이 비어있거나 닫는 괄호가 아니면 계속 arr의 문자열을 스택에 쌓는다.
arr[i]가 닫는 괄호면, 괄호 안의 문자열을 임의로 저장하기위한 tmp배열을 만든다.
스택에서 top이 여는 괄호가 될때까지 pop하여 tmp에 추가하고, 마지막으로 여는 괄호도 스택에서 제거해준다.

이렇게 하면 괄호 안의 문자열이 뒤집힌 상태로 tmp에 저장되어 있다.
tmp를 스택의 top 즉, 여는 괄호 바로 왼쪽에 있던 숫자와 곱한다. (배열 곱셈)
이 후, tmp를 오른쪽부터 스택에 쌓아주면 올바른 순서대로 스택에 저장된다.

모든 탐색이 끝나면 stk의 길이를 출력하면 압축되지 않은 문자열의 길이가 된다.
'''
            
