INFINITY = 999999


def printTable(d):
    print("Node  ", "Shortest Distance", sep="")
    for i in range(len(nodesList)):
        print(f"{nodesList[i]:<6}", f"{d[i]:<17}")
    print('')


def BellmanFord(graph, source=0):
    d = [INFINITY for i in range(n)]
    d[source] = 0

    for k in range(n-1):
        for u, v, w in graph:
            if d[u] != INFINITY and d[u] + w < d[v]:
                d[v] = d[u] + w
            if d[v] != INFINITY and d[v] + w < d[u]:
                d[u] = d[v] + w
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

for source in range(n):
    BellmanFord(graph, source)


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
