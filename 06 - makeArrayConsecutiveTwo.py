'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

  For statues = [6, 2, 3, 8], the output should be
  solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.
'''

def solution(statues):
    statues.sort()
    statuesNeeded = 0
    for i in range(0, len(statues)-1):
        if(statues[i + 1] - statues[i]) > 1:
            statuesNeeded = statuesNeeded + statues[i + 1] - statues[i] - 1
    print(f'Status needed {statuesNeeded}')
    return statuesNeeded
  
 
solution([0, 3])
