# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
tree1 = (1, (2, None, (4, None, None)), (3, (5, (7, None, None), (8, None, None)), (6, (9, None, None), (10, (11, None, None), None))))
tree2 = (1, (2, (4,
                    (8, (12, None, None), (13, None, None)),
                    (9, (14, None, None), (15, None, None))
                 ),
                (5,
                    (10, (16, None, None), (17, None, None)),
                    (11, (18, None, None), (19, None, None)),
                 )),
            (3, (6, None, None),
                (7, None, None)))


def is_perfect(node, level = 3):

    if not node:
        return False
    if not node[1] and not node[2]:
        if level == 0:
            return True
        return False

    if level != 0:
        left = is_perfect(node[1], level-1)
        right = is_perfect(node[2], level-1)

        if (left and right):
            return True
        else:
            return False
    else:
        return True



def traverse(node, maximum=0, level_max = 100):

    if node is None:
        return maximum


    for level in range(1,level_max+1):
        trial = is_perfect(node,level)
        if trial and not(not node[1] and not node[2]):
            nodes = (2**(level+1)) - 1
            if nodes > maximum:
                maximum = nodes
        else:
            break

    left = traverse(node[1], maximum)
    if left > maximum:
        maximum = left
    right = traverse(node[2], maximum)
    if right > maximum:
        maximum = right
    return maximum


def solution(T):
    return(traverse(T))

print(solution(tree1))
print(solution(tree2))