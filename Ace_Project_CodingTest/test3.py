# 영희는 게임 캐릭터입니다.

# 게임 내에서 영희는 시간 순서대로 n개의 물약을 먹게 됩니다.

# i번째 물약(i = 1, 2, 3, ..., n)은 시간 t_i에 먹게 되는데, 이 물약을 먹으면 다음 시간부터 매 시간마다 effect_i만큼 체력(hp)이 변화하게 됩니다.

# 예를 들어서 시간 t_i = 5에 effect_i = -3짜리 물약을 먹었으면, 시간 6부터 매 시간마다 체력이 계속 3씩 줄어들게 됩니다.

# 영희의 체력은 항상 0 이상 maxhp 이하의 정수입니다.

# 물약의 효과 때문에 체력이 maxhp보다 커질 것처럼 된다면 체력은 maxhp로 설정됩니다. 마찬가지로 물약의 효과 때문에 체력이 0보다 작아질 것처럼 되어도 체력은 0으로 설정됩니다.

# 체력이 0이 되어도 영희는 죽지 않습니다.

# 물약의 효과는 항상 누적되기 때문에 기존에 먹은 물약의 효과가 새로운 물약을 먹을 때 사라지거나 하지 않습니다.

def solution(n, maxhp, times, effects):
    answer = 0
    time = -1
    cur_index = 0
    sum_effects = 0
    hp = 0
    while True:
        if times[cur_index] == time:
            sum_effects += effects[cur_index]
            if cur_index < n - 1:
                cur_index += 1
            time += 1
        else:
            time += 1

        if time > times[-1] and sum_effects > 0:
            break

        hp += sum_effects

        if hp < 0:
            hp = 0

        if hp > maxhp:
            hp = maxhp

        #print(time, " : ", hp)

        if hp == 0 or hp == maxhp:
            answer += 1 

    return answer

print(solution(5, 10, [1,5,7,10,11], [4,-6,-1,4,1]))

