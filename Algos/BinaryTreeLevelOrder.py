# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


import copy
from collections import deque

def levelOrder(self, root):
    
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root])
    while queue:
        levels.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels
