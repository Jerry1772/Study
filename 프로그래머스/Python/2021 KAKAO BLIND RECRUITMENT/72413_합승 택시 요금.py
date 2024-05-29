# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq
def dijkstra(g, s):
    ds = {node: 1000000 for node in g}
    ds[s] = 0
    q = []
    heapq.heappush(q, [ds[s],s])
    while q:
        c_d, c_node = heapq.heappop(q)
        if ds[c_node] < c_d:
            continue
        for a, w in g[c_node].items():
            d = c_d + w
            if d<ds[a]:
                ds[a] = d
                heapq.heappush(q, [d, a])
    return ds
def solution(n, s, a, b, fares):
    graph = {i:{} for i in range(1,n+1)}
    for i,j,k in fares:
        graph[i][j]=k
        graph[j][i]=k
    dist = {i:dijkstra(graph,i) for i in range(1,n+1)}
    fare = dist[s][a]+dist[s][b]
    for i in range(1,n+1):
        fare = min(dist[s][i]+dist[i][a]+dist[i][b], fare)
    return(fare)

if __name__ == "__main__":
    param = {
        "n": 6,
        "s": 4,
        "a": 6,
        "b": 2,
        "fares": 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    }
    result = 82
    print(solution(**param), result)