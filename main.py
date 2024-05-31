import itertools
import heapq


class TSP:
    def __init__(self, distances):
        self.distances = distances
        self.num_cities = len(distances)
        self.best_cost = float('inf')
        self.best_path = []

    def dfs(self):
        def dfs_util(current_city, visited, current_cost, path):
            if len(visited) == self.num_cities:
                total_cost = current_cost + self.distances[current_city][path[0]]
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_path = path + [path[0]]
                return

            for next_city in range(self.num_cities):
                if next_city not in visited:
                    visited.add(next_city)
                    dfs_util(next_city, visited, current_cost + self.distances[current_city][next_city],
                             path + [next_city])
                    visited.remove(next_city)

        for start_city in range(self.num_cities):
            dfs_util(start_city, {start_city}, 0, [start_city])

    def ucs(self):
        pq = [(0, 0, [0])]
        while pq:
            current_cost, current_city, path = heapq.heappop(pq)
            if len(path) == self.num_cities:
                total_cost = current_cost + self.distances[current_city][path[0]]
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_path = path + [path[0]]
                continue

            for next_city in range(self.num_cities):
                if next_city not in path:
                    heapq.heappush(pq, (
                    current_cost + self.distances[current_city][next_city], next_city, path + [next_city]))

    def astar(self):
        def heuristic(city, visited):
            unvisited_cities = [self.distances[city][next_city] for next_city in range(self.num_cities) if
                                next_city not in visited]
            return min(unvisited_cities) if unvisited_cities else 0

        pq = [(0 + heuristic(0, {0}), 0, 0, [0])]
        while pq:
            _, current_cost, current_city, path = heapq.heappop(pq)
            if len(path) == self.num_cities:
                total_cost = current_cost + self.distances[current_city][path[0]]
                if total_cost < self.best_cost:
                    self.best_cost = total_cost
                    self.best_path = path + [path[0]]
                continue

            for next_city in range(self.num_cities):
                if next_city not in path:
                    next_cost = current_cost + self.distances[current_city][next_city]
                    heapq.heappush(pq, (next_cost + heuristic(next_city, set(path) | {next_city}), next_cost, next_city,
                                        path + [next_city]))

    def solve(self):
        self.best_cost = float('inf')
        self.best_path = []
        print("Solving with DFS...")
        self.dfs()
        print(f"DFS Best Cost: {self.best_cost}, Path: {self.best_path}")

        self.best_cost = float('inf')
        self.best_path = []
        print("Solving with UCS...")
        self.ucs()
        print(f"UCS Best Cost: {self.best_cost}, Path: {self.best_path}")

        self.best_cost = float('inf')
        self.best_path = []
        print("Solving with A*...")
        self.astar()
        print(f"A* Best Cost: {self.best_cost}, Path: {self.best_path}")



distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp = TSP(distances)
tsp.solve()
