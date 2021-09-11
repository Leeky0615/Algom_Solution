from collections import deque


class Node:
    def __init__(self, data, left, right, val):
        self.data = data
        self.left = left
        self.right = right
        self.val = val
        self.visited = False


def solution(info, edges):
    answer = 0
    temp = [[] for _ in range(len(info))]
    for e in edges:
        node, child = e[0], e[1]
        temp[node].append(child)
    print(temp)
    tree = {}
    for idx, data in enumerate(temp):
        print(idx)
        if data:
            left = data[0] if data[0] else None
            right = data[1] if len(data) == 2 else None
            tree[idx] = Node(idx, left, right, info[idx])

    tree[0].visited = True
    dfs(tree, tree[0], 0)
    return answer


def dfs(tree, v, result):
    v.visited = True
    if not v.visited:
        if v.val:
            result += 1
        else:
            result -= 1




info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

print(solution(info, edges))


def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end=' ')
    if node.right != None:
        in_order(tree[node.right])


# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end=' ')