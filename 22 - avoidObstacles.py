'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.
'''
def solution(inputArray):
    obs = sorted(inputArray)
    jump_dist = 1
    obstacle_hit = True
  
    while(obstacle_hit):          
        obstacle_hit = False
        jump_dist += 1
    
        for i in range(0, len(obs)):
            if obs[i] % jump_dist == 0:             
                obstacle_hit = True
                break
  
    return jump_dist
