# 정수로 이루어진 배열이 있습니다.

# 배열을 좌우 두 부분으로 갈랐을 때, 각 배열의 원소의 합 간 차이를 최소로 하려고 합니다.

# 이렇게 차이를 최소화하도록 갈랐을 때, 왼쪽 배열의 원소의 개수를 반환하는 함수를 작성해 주세요.

# 만약 차이를 최소화하는 방법이 여러 가지가 있다면 왼쪽 배열의 원소의 개수를 최소화하는 답을 반환하세요.

# 한쪽 배열을 비워 두는 것도 가능하며, 빈 배열의 원소의 합은 0으로 정의합니다.

def solution(n, v):
    answer = 0
    _min = 0

    for i in range(0, n + 1):
        sum_left = sum(v[:i])
        sum_right = sum(v[i:])
        
        if i == 0:
            _min = abs(sum_left - sum_right)
        else:
            if _min > abs(sum_left - sum_right):
                _min = abs(sum_left - sum_right)
                answer = i
    return answer

print(solution(5, [1,2,1,2,1]))