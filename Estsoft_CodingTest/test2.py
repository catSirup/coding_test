# In an old drawer of your desk, you have found some long-forgotten necklaces. Each necklace comprises a number of beautiful, once shiny, beads. Unfortunately, now they are not only dusty, but also tangled together. You remember that the necklace with the most beads used to be your favorite. Now, you are interested in finding the necklace with the largest number of beads, without having to untangle them all .

# You have carefully photographed the necklaces and numbered all the beads with numbers in the range [0... N-1], so that each number corresponds to exactly one bead. Then, for each bead, you have found the number of the next bead following it.

# This information is given as an array of integers, indexed by bead numbers, and the elements are the numbers of the following beads. Each bead number appears in the array exactly once.

# that, given an array A consisting of N integers, as described above, returns the maximum number of beads in a single necklace. The function should return 0 if the array is empty.

# For example, given array A such that:
# A[0] = 5
# A[1] = 4
# A[2] = 0
# A[3] = 3
# A[4] = 1
# A[5] = 6
# A[6] = 2

# the function should return 4, because the longest necklace is the one containing four beads: numbers {0, 5, 6, 2}. Presented below are the untangled necklaces

# Write an efficient algorithm for the following assumptions:

# 1) N is an integer within the range 0 to 1,000,000
# 2) the elements of A are all distinct
# 3) each element of array A is an integer within the range 0 to N-1


# 인덱스와 비드 넘버가 서로 같은 애들을 찾는 게 문제
# 저기서는 1번과 4번이 서로 같은 것을 공유하기 때문에 두 개가 목걸이
import time
import random

def solution(A):
    answer = 0
    # 배열의 길이만큼 False로 새로운 배열을 하나 생성
    checklist = [False for _ in range(len(A))]
    countList = []
    
    for i in range(len(A)):
        #print("---", i, "번째 루프----")
        if checklist[i] == False:
            tempCount = 0
            tempNum = i
            while True:
                if A[tempNum] != i:
                    checklist[tempNum] = True
                    tempNum = A[tempNum]
                    tempCount += 1
                else:
                    tempCount += 1
                    checklist[tempNum] = True
                    countList.append(tempCount)
                    #print(checklist)
                    break

        else:
            #print(i,"는 이미 체크함")
            continue

    if len(countList) != 0:
        answer = max(countList)
    return answer

# testlist = []
# for i in range(99999):
#     testlist.append(i)

# random.shuffle(testlist)
# print(testlist)

start_vect=time.time()
print(solution([5, 4, 0, 3, 1, 6, 2]))
# print(solution(testlist))
# print(solution([3, 6, 5, 0, 8, 2, 7, 9, 1, 4]))
print("training Runtime: %0.6f Minutes"%((time.time() - start_vect)/60))
