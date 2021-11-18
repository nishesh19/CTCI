from collections import defaultdict, deque


def has_common_ancestor(parent_child_pairs, p1, p2):
    child_to_parent = defaultdict(list)
    for parent, child in parent_child_pairs:
        child_to_parent[child].append(parent)

    def dfs(visited: set, child: int):

        for parent in child_to_parent[child]:
            visited.add(parent)
            dfs(visited,parent)

    p1_ancestors = set()
    p2_ancestors = set()

    dfs(p1_ancestors,p1)
    dfs(p2_ancestors,p2)

    # p1_ancestors.remove(p1)
    # p2_ancestors.remove(p2)
    return bool(p1_ancestors & p2_ancestors)


parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

print(has_common_ancestor(parent_child_pairs, 3, 8))
print(has_common_ancestor(parent_child_pairs, 5, 8))
print(has_common_ancestor(parent_child_pairs, 6, 8))
print(has_common_ancestor(parent_child_pairs, 6, 9))
print(has_common_ancestor(parent_child_pairs, 1, 3))
print(has_common_ancestor(parent_child_pairs, 3, 1))
print(has_common_ancestor(parent_child_pairs, 7, 11))
print(has_common_ancestor(parent_child_pairs, 6, 5))
print(has_common_ancestor(parent_child_pairs, 5, 6))
