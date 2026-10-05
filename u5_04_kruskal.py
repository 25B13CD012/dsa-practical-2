def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def kruskal(n, edges):
    parent = list(range(n))
    mst = []
    total = 0

    for w, u, v in sorted(edges):
        ru = find(parent, u)
        rv = find(parent, v)

        if ru != rv:
            parent[ru] = rv
            mst.append((u, v, w))
            total += w
            print(f"Add edge {u}-{v} (w={w})")
        else:
            print(f"Skip edge {u}-{v} (w={w}) - forms a cycle")

    return mst, total


edges = [
    (4, 0, 1),
    (8, 0, 2),
    (2, 1, 2),
    (6, 1, 3),
    (3, 2, 3),
    (5, 2, 4),
    (7, 3, 4)
]

mst, total = kruskal(5, edges)

print("MST weight:", total)
