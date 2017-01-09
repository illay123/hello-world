import numpy as np
import random

inf = float('Inf')


def fx(x, i, j):
    return x+i-i+j-j


def graph_generator(decrese_function, size: int = 1, con_pro: float = 1, expectation: float = 10, standard_deviation: float = 3):
    graph = [inf] * size
    i = 0
    while i < size:
        graph[i] = [inf] * size
        i += 1

    i = 0
    j = 0
    while i < size:
        while j < size:
            if con_pro > decrese_function(random.random(), i, j):
                graph[i][j] = np.random.normal(expectation, standard_deviation, None)
            if i == j:
                graph[i][j] = 0
            j += 1

        j = 0
        i += 1
    return graph


def dijkstra(starting_point, dis_graph):
    i = 0
    # delta = np.empty(len(dis_graph))
    delta = [0] * len(dis_graph)
    while i < len(dis_graph):
        delta[i] = dis_graph[starting_point][i]
        i += 1

    while True:
        # print(delta,i)
        if listCompare(upgrade(delta, dis_graph), delta):
            break
        delta = upgrade(delta, dis_graph)
    return delta


def listCompare(a, b):
    # print ("a[0]=",a[0])
    if len(a) != len(b):
        return False
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
        i += 1
    return True


def upgrade(delta, dis_graph):
    i = 0
    j = 0
    while i < len(dis_graph):
        j = 0
        while j < len(dis_graph):
            if delta[i] > delta[j] + dis_graph[j][i]:
                delta[i] = delta[j] + dis_graph[j][i]
            j += 1
        i += 1
    # print (delta)
    return delta

def dynamicLength(dis_graph, taxi_starting_point, orders, waze):
    i = 0
    total = dijkstra(taxi_starting_point, dis_graph)[waze[orders[0]][0]]
    while i < len(orders) - 1:
        total += dijkstra(waze[orders[i]][1], dis_graph)[waze[orders[i+1]][0]]  # find the distance from the destination of the i person in the list to the starting point of the next one
        i += 1
    #print("dl", total, orders)
    return total

def staticLength(dis_graph, waze):
    i = 0
    total = 0
    while i < len(waze):
        total += dijkstra(waze[i][0], dis_graph)[waze[i][1]]
        i += 1
    return total


def solve(dis_graph, waze, taxi_starting_point):
    a = []
    return minimum(dis_graph, waze, taxi_starting_point, a) + staticLength(dis_graph, waze)


def minimum(dis_graph, waze, taxi_starting_point, a):
    if len(a) == len(waze):
        return dynamicLength(dis_graph, taxi_starting_point, a, waze)
    else:
        left_number = []
        i = 0
        while i < len(waze):
            left_number.append(i)
            i += 1
        i = 0
        while i < len(a):
            try:
                left_number.remove(a[i])
            except ValueError:
                pass
            i += 1
        m = inf
        i = 0
        #print("m", left_number)
        while i < len(left_number):
            a.append(left_number[i])
            new = minimum(dis_graph, waze, taxi_starting_point, a)
            if m > new:
                m = new
            a.remove(left_number[i])
            i += 1
        #print(m)
        return m


try_graph = np.array([
[0,6,inf,5],
[6,0,5,inf],
[7,inf,0,3],
[inf,4,inf,0]
])

aze = [(0, 2), (1, 3)]

print(solve(try_graph, aze, 3))

# print("status:")
# print("graph:\n",try_graph)
# print("taxi starting at 3")
# print("persons roads:\n",aze)
# print("0,1 -> ", dynamicLength(try_graph, 3, [0, 1], aze), "<?>")
# print("1,0 -> ", dynamicLength(try_graph, 3, [1, 0], aze))
# print("stat", staticLength(try_graph, aze))

# print()
# print (dijkstra(0,try_graph))

# print (try_graph)
# real_dis_graph = try_graph.copy()
# real_dis_graph[:] = inf
# print (real_dis_graph)
# print(graph_generator(fx, 9, 0.5, 10, 3))
