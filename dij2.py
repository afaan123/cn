INFINITY = 999999


def printTable(d):
    print("Node  ", "Shortest Distance", sep="")
    for i in range(len(nodesList)):
        print(f"{nodesList[i]:<6}", f"{d[i]:<17}")
    print('')


def Djikstra(edgeList, source):
    cost = [[INFINITY for i in range(n)] for j in range(n)]
    for u, v, w in edgeList:
        cost[u][v] = w
        cost[v][u] = w

    d = cost[source][:]
    d[source] = 0
    # at this point, d(0, j) will be edge cost, if there is a direct edge between 0 and j, else it will be INFINITY

    visited = []
    while len(visited) != n:
        # there are still nodes left to be visited
        minimum = INFINITY
        min_node = -1
        for i in range(n):
            if i not in visited and d[i] < minimum:
                minimum = d[i]
                min_node = i
        
        visited.append(min_node)
        for dest in range(n):
            if cost[min_node][dest] != INFINITY and dest not in visited:
                if d[dest] > d[min_node] + cost[min_node][dest]: 
                    d[dest] = d[min_node] + cost[min_node][dest]

    printTable(d)


n = int(input('Enter number of nodes: '))
graph = []
nodesList = input('Enter Node Names: ').strip().split(" ")

print('Enter Edges in the form of (A,B,w), which means an edge of weight, w from A to B: ')
print('Enter "end" to stop entering edges')
print("Enter node names in capital letters")
print('If any Edge cost is infinity, please enter the value as "inf"\n')

count = 1
inp = input(f"Enter Edge {count} (eg. A B 2): ").strip()
while inp != "end":
    count += 1
    try:
        source, destination, weight = inp.split(" ")
        if weight == "inf":
            weight = INFINITY
        graph.append((nodesList.index(source), nodesList.index(destination), int(weight)))
    except:
        print("Invalid input! Try again...")
    inp = input(f"Enter Edge {count} (eg. A B 2): ").strip()

print("")
source = nodesList.index(input("Enter source vertex: "))
Djikstra(graph, source)

# eg inputs
# 6
# R1 R2 R3 R4 R5 R6
# R1 R2 6
# R1 R3 3
# R2 R3 2
# R2 R4 7
# R4 R5 1
# R3 R5 9
# R4 R6 8
# R5 R6 4
# end
