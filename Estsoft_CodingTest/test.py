# In the army, each soldier has an assigend rank. A soldier of rank X has to report to (any) soldier of rank (X + 1). many soldiers can report to the same superior. write a function:

# that, give an array ranks consisting of soldiers' ranks, return the number of soldiers who can report to some superior.

# Examples:

# 1. Given ranks = [3, 4, 3, 0, 2, 2, 3, 0, 0], your function should return 5, because: 
# 1) three soldiers of rank 3 (RANKS[0], RANKS[2], RANKS[6]) may report to a soldier of rank4(RANKS[1])
# 2) Tow soldiers of rank 2 may report to any soldier of rank 3.

# 2. Given ranks = [4, 2 ,0], your function should return 0.

# 3. Given ranks = [4, 4, 3, 3, 1, 0], your function should return 3, because:

# 1) A soldier of rank 0 can report to soldier of rank 1
# 2) Two soldiers of rank 3 can report to any soldier of rank 4

# Write an efficient algorithm for the following assumptions:

# 1) N is an integer within the range[2...100,000];
# 2) each element of array ranks is an integer within the range[0...1,000,000,000].
import time

start_vect=time.time()

def solution(ranks):
    answer = 0
    sortedList = sorted(ranks)
    flag = 0
    for i in sortedList:
        if i == sortedList[0]:
            flag = i

        elif i == (flag + 1):
            answer += sortedList.count(flag)
            flag = i

        elif i != flag and i != flag + 1:
            flag = i

    return answer

#print(solution([3, 4, 3, 0, 2, 2, 3, 0, 0]))
#print(solution([4, 2, 0]))
#print(solution([4, 4, 3, 3, 1, 0]))
print("answer: ", solution([100000, 600, 456, 123, 34534, 34234, 99999, 8989, 6483, 1, 2, 3, 4, 5, 5, 6, 7]))
print("training Runtime: %0.6f Minutes"%((time.time() - start_vect)/60))