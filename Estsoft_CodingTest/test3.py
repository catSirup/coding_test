import numpy as np

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

def cango(B, gameMap, character_index):
    answer = ''

    # 오른쪽 대각선만 가능
    if ((character_index[1] != len(B) - 2 and gameMap[character_index[0] - 1][character_index[1] + 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] + 2] == '.') == True \
        and ((character_index[1] != 1 and gameMap[character_index[0] - 1][character_index[1] - 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] - 2] == '.' ) == False:
        answer = 'case1'
    # 왼쪽 대각선만 가능
    elif ((character_index[1] != len(B) - 2 and gameMap[character_index[0] - 1][character_index[1] + 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] + 2] == '.') == False \
        and ((character_index[1] != 1 and gameMap[character_index[0] - 1][character_index[1] - 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] - 2] == '.' ) == True:
        answer =  'case2'
    # 양쪽 모두 가능
    elif ((character_index[1] != len(B) - 2 and gameMap[character_index[0] - 1][character_index[1] + 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] + 2] == '.') == True \
        and ((character_index[1] != 1 and gameMap[character_index[0] - 1][character_index[1] - 1] == 'x') \
        and gameMap[character_index[0] - 2][character_index[1] - 2] == '.' ) == True:
        answer =  'case3'
    # 양쪽 모두 불가능
    else:
        answer =  'case4'

    return answer

def solution(B):
    answer = 0
    temp = []
    
    for line in B:
        for text in list(line):
            temp.append(text)

    # numpy 배열로 맵 재정리
    gameMap = np.array(temp).reshape(len(B), len(B))
    character_index = []
    aladdins_index = []

    for i in range(len(B)):
        for j in range(len(B)):
            if gameMap[i][j] == 'o':
                character_index.append(i)
                character_index.append(j)
            
            if gameMap[i][j] == 'x':
                aladdins_index.append((i, j))

   
    print(gameMap)

    # 서치를 돌릴 때, 두 곳 모두 갈 수 있는 곳일 경우,
    # 그래프에 넣어서 두 인덱스들을 저장해놓고
    # 깊이 우선 탐색으로 돌려야할 것 같은데
    # 노드를 매번 동적으로 붙여넣어도 되는건가

    # 일단 맵 변경안되도록 카피
    gmap = gameMap
    # 이 맵을 가지고 우선 갈 수 있는 인덱스들을 쫙 다 넣고 노드로 연결해야하나...      
    # 노드간 경로 탐색이 제일 긴 놈을 고르면 된다?
    while True:
        if cango(B, gmap, character_index) == 'case1':
            break
        if cango(B, gmap, character_index) == 'case2':
            break
        if cango(B, gmap, character_index) == 'case3':
            break
        if cango(B, gmap, character_index) == 'case4':
            break


    return answer

print (solution(["..x...", "......", "....x.", ".x....", "..x.x.", "...o.."]))