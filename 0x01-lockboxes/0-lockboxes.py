#!/usr/bin/python3
"""Contains function canUnlockAll"""


def canUnlockAll(boxes):
    """
    Breadth-First search Algorithm to determine if all boxes can be opened
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
