#include <iomanip>
cout<<sflags(ios::fixed)<<setprecision(2)<<result<<endl;

DFS https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def dfs(paths, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(paths[node] - visited)
    return visited

def dfs(paths, start, target):
    if start == target:
        return [start]
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for next_id in range(len(paths[node])):
            next_node = paths[node][next_id]
            to = next_node.to
            if to not in set(path):
                if to == target:
                    return path + [to]
                else:
                    stack.append((to, path + [to]))

def bfs(paths, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop(0)
        if node not in visited:
            visited.add(node)
            stack.extend(paths[node] - visited)
    return visited

def bfs(paths, start, target):
    if start == target:
        return start
    else:
        stack = [(start, [start])]
        while stack:
            (node, path) = stack.pop(0)
            for next_node in paths[node] - set(path):
                if next_node == target:
                    return path + next_node
                else:
                    stack.append((next_node, path + [next_node]))


Bellman-Fold: negative_edges

MST http://www.guofei.site/2017/09/12/minimumspanningtree.html
