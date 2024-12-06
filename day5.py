from sys import stdin
import re
from collections import defaultdict
from collections import deque

sequences = []
queries = []

with open("input.txt") as file:
    for line in file:
        l = line.strip()
        sp = l.split("|")
        if l == "":
            continue
        if len(sp) == 2:
            sequences.append([int(sp[0]), int(sp[1])])
        else:
            queries.append([int(x) for x in l.split(",")])


prev = defaultdict(set)
post = defaultdict(set)
for a, b in sequences:
    prev[b].add(a)
    post[a].add(b)


# brute force to check if query is valid
def valid(query):
    for i in range(len(query)):
        for j in range(i + 1, len(query)):
            if query[j] not in post[query[i]]:
                return False
    return True


# topological sort
# not exactly sure what happens when there are different orderings
# but test case was not generated in that way
def get_order(query):
    d = defaultdict(int)
    q = deque()
    # create smaller graph with just numbers in query
    for i in query:
        for o in prev[i]:
            if o in query:
                d[i] += 1

    # indeg 0 numbers
    for i in query:
        if i not in d:
            q.append(i)

    # topo sort
    vis = []
    while q:
        cur = q.popleft()
        if cur in vis:
            continue
        vis.append(cur)
        for adj in post[cur]:
            if adj in d:
                d[adj] -= 1
                if d[adj] <= 0:
                    q.append(adj)

    # return middle
    return vis[len(vis) // 2]


ans = 0

for q in queries:
    if not valid(q):
        ans += get_order(q)

print(ans)
