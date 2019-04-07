# 영어 소문자로만 이루어진 문자열이 있습니다.

# 사전순으로 가장 뒤에 오는 부분 문자열을 반환하는 프로그램을 작성하세요.

# 부분 문자열이란, 원래 문자열의 각 문자 중 일부를 택하여 만들 수 있는 문자열을 의미합니다. 이 때, 택한 문자가 꼭 연속할 필요는 없지만 원래 문자열에서의 순서는 유지해야 합니다. 빈 문자열은 부분 문자열이 아닙니다.

# 사전순은 다음과 같이 정의됩니다.

# 두 문자열의 첫 번째 문자부터 비교하여 처음으로 다른 문자를 발견합니다.
# 처음으로 다른 문자가 더 큰 문자열이 사전순으로 더 뒤가 됩니다.
# 처음으로 다른 문자를 발견하기 전에 한 문자열의 문자가 모두 소진된 경우 (즉, 한 문자열이 다른 문자열의 접두어인 경우) 길이가 더 긴 문자열이 사전순으로 더 뒤가 됩니다.
# a, aa, aba, abc, abcd, b, baa, baab는 문자열들을 사전순으로 나열한 한 예입니다.

from itertools import combinations

def solution(s):
    answer = ''
    temp = []
    for i in range(1, len(s) + 1):
        temp += list(map(''.join, set(combinations(s, i))))

    temp.sort()
    answer = temp[-1]
    
    return answer

print(solution('baba'))