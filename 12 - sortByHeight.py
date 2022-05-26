'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190]
'''

def sortByHeight(a):
    tree_pos = [i for i in range(len(a)) if a[i] == -1]
    peeps_pos = [i for i in a if i != -1]
    peeps_pos.sort()
    for tree in tree_pos:
        peeps_pos.insert(tree, -1)
    
    return peeps_pos
  
  sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]
