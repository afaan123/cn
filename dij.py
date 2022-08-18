
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

source=input('Enter Source Node: ').upper()
visited=[]
for node in edges[source]:
    shortest_dist[node]=cost[node+source]

visited.append(source)
shortest_dist[source]=0

while(len(visited)!=n):
    min=999999
    min_node=''
    for node in nodes:
        if node not in visited:
            if shortest_dist[node]<min:
                min=shortest_dist[node]
                min_node=node
    
    visited.append(min_node)
    for node in edges[min_node]:
        if node not in visited:
            if shortest_dist[node]>shortest_dist[min_node]+cost[min_node+node]:
                shortest_dist[node]=shortest_dist[min_node]+cost[min_node+node]

print('')
print('Node', end='    ')
print('Shortest Distance')
for node in shortest_dist.keys():
    print(' ',node,'          ',shortest_dist[node])