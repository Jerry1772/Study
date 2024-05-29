# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    import heapq
    graph = {}
    for a,b,c in road:
        if a in graph: graph[a].append([b,c])
        else: graph[a]=[[b,c]]
        if b in graph: graph[b].append([a,c])
        else: graph[b]=[[a,c]]

    distances = {i:float('inf') for i in range(1,N+1)}
    distances[1]=0

    queue = []
    heapq.heappush(queue, [0,1])

    while queue:
        c_dist, c_node = heapq.heappop(queue)
        if c_dist > distances[c_node]: continue

        for n_node, n_dist in graph[c_node]:
            dist = distances[c_node]+n_dist
            if dist < distances[n_node]:
                distances[n_node] = dist
                heapq.heappush(queue, [dist,n_node])
    answer = 0
    for d in distances:
        if distances[d]<=K:answer+=1
    return answer

if __name__ == "__main__":
    param = {
        "N": 5,
        "road": [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],
        "K": 3
    }
    result = 4
    print(solution(**param), result)