def BellmanFord(source,nodes,edges,cost):
    print('')
    print('Node ',source)
    print('')
    shortest_dist={}
    for i in range(len(nodes)):
        shortest_dist[nodes[i]]=999999
    for node in edges[source]:
        shortest_dist[node]=cost[source+node]
    shortest_dist[source]=0
    print('Initial:')
    print('')
    print('Node', end='    ')
    print('Shortest Distance')
    for node in shortest_dist.keys():
        print(' ',node,'          ',shortest_dist[node])
    print('')
    for k in range(2,n):
        for node in nodes:
            if node!=source and len(edges[node])!=0:
                for other_node in edges[node]:
                    if shortest_dist[node]>shortest_dist[other_node]+cost[node+other_node]:
                        shortest_dist[node]=shortest_dist[other_node]+cost[node+other_node]
        print('Step ',k,':')
        print('')
        print('Node', end='    ')
        print('Shortest Distance')
        for node in shortest_dist.keys():
            print(' ',node,'          ',shortest_dist[node])
        print('')
    

n=int(input('Enter number of nodes: '))
print('Enter Node Names:')
nodes=[]
edges={}
cost={}
shortest_dist={}

for i in range(n):
    nodes.append(input(f'Node {i+1}: ').upper())
    edges[nodes[i]]=[]
    shortest_dist[nodes[i]]=999999

count=0
print('Enter Edges: ')
print('Note: Enter edge as end,end to stop entering more edges\nEnter Node names in Capital Letters')
print('If any Edge cost is infinity, please enter the value as 99999')
print('')
s=d=''
while s.lower()!='end' and d.lower()!='end':
    print('Edge ',count+1,':')
    s=input('Enter source node: ')
    d=input('Enter destination node: ')
    if s!='end' and d!='end':
        c=float(input('Enter cost of edge: '))
        edges[s].append(d)
        edges[d].append(s)
        cost[s+d]=cost[d+s]=c
    print('')
    count+=1

for source in nodes:
    BellmanFord(source,nodes,edges,cost)
