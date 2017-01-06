import numpy as np
inf = float('Inf')

def dijkstra(starting_point,dis_graph):
	i = 0
	#delta = np.empty(len(dis_graph))
	delta = [0]*len(dis_graph)
	while i< len(dis_graph):
		delta[i] = dis_graph[starting_point][i]
		i+=1

	i = 0
	while True:
		print(delta,i)
		if listCompare(upgrade(delta,dis_graph),delta):
			break
		delta = upgrade(delta,dis_graph)
	return delta

def listCompare (a,b):
	print ("a[0]=",a[0])
	if (len(a) != len(b)):
		return False
	i = 0
	while i < len (a):
		if(a[i] != b[i]):
			return False
		i+=1
	return True
        

def upgrade (delta,dis_graph):
	i = 0
	j = 0
	while i< len(dis_graph):
		j = 0
		while j< len(dis_graph):
			if delta[i] > delta[j] + dis_graph[j][i]:
				delta[i] = delta[j] + dis_graph[j][i]
			j+=1
		i+=1
	print (delta)
	return delta

# graph = [
# [0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0,inf],
# [inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,inf,0],
# ]

try_graph = np.array([
[0,6,inf,5],
[6,0,5,inf],
[7,inf,0,3],
[inf,4,inf,0]
])

waze = [(1,2),(7,14)]
# print (try_graph)
# real_dis_graph = try_graph.copy()
# real_dis_graph[:] = inf
# print (real_dis_graph)
print()
print (dijkstra(0,try_graph))