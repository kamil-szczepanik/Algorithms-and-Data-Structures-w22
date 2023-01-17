import sys
from queue import PriorityQueue
import math


class Graph:
    def __init__(self, filename):
        self.map = self.get_map(filename)
        self.zeros = self.find_start_and_end(self.map)
        self.width = len(self.map[0])
        self.height = len(self.map)

    def get_map(self, filename):

        with open(filename, 'r', encoding='utf-8') as file:
            m = [[int(c) for c in line.strip()] for line in file.readlines()]
        return m

    def find_start_and_end(self, map):
        zeros = []
        for y, row in enumerate(map):
            for x, num in enumerate(row):
                if num==0:
                    zeros.append((x,y))
        if len(zeros) != 2:
            raise Exception("Incorrect map!")
        return zeros

    def neighbours(self, point):
        x, y = point
        return [(p, self.map[p[1]][p[0]]) for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if p[0] >= 0 and p[0]<self.width and p[1] >= 0 and p[1]<self.height]
        

    def shortest_path_dijkstra(self):
        start, end= self.zeros[0], self.zeros[1]
        costs = {start: 0}

        # do kolejki priorytetowej dodajemy punkt startowy z kosztem 0
        # kolejka priorytetowa zwraca punkty (ścieżki) o najniższym koszcie
        pq = PriorityQueue()
        pq.put((0, start, [start]))

        while pq.qsize()>0:
            cost, point, path = pq.get()

            if point == end:
                return path

            # sprawdzenie sąsiadów
            for neighbour, neighbour_cost in self.neighbours(point):
                neighbour_cost += cost

                # jezeli droga jest lepsza to dodajemy do kolejki
                if neighbour_cost < costs.get(neighbour, math.inf):
                    costs[neighbour] = neighbour_cost
                    pq.put((neighbour_cost, neighbour, path + [neighbour]))

    def print_path(self, path):

        result_map = [[" "]*self.width for _ in range(self.height)]

        for point in path:
            x, y = point
            result_map[y][x] = str(self.map[y][x])

        print("\n".join("".join(row) for row in result_map))

    def calculate_path_cost(self, path):
        cost = 0
        for point in path:
            x, y = point
            cost += self.map[y][x]
        return cost


if __name__=="__main__":
    filename = sys.argv[1]

    graph = Graph(filename)
    path = graph.shortest_path_dijkstra()
    graph.print_path(path)



