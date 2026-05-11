import heapq

class FlightRoutePlanner:
    def __init__(self):
        self.graph = {}

    def add_airport(self, airport):
        if airport not in self.graph:
            self.graph[airport] = {}

    def add_route(self, from_airport, to_airport, distance, time):
        self.add_airport(from_airport)
        self.add_airport(to_airport)

        self.graph[from_airport][to_airport] = {
            "distance": distance,
            "time": time
        }

    def show_routes(self):
        print("Available Flight Routes:")
        for airport in self.graph:
            print(f"\nFrom {airport}:")
            if self.graph[airport]:
                for destination, info in self.graph[airport].items():
                    print(f"  -> {destination} | Distance: {info['distance']} km | Time: {info['time']} min")
            else:
                print("  No outgoing routes")

    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            print("Airport not found.")
            return

        queue = [(0, start, [])]
        visited = set()

        while queue:
            current_time, current_airport, path = heapq.heappop(queue)

            if current_airport in visited:
                continue

            visited.add(current_airport)
            path = path + [current_airport]

            if current_airport == end:
                print("\nShortest Route Found:")
                print(" -> ".join(path))
                print(f"Total Time: {current_time} minutes")
                return

            for neighbor, info in self.graph[current_airport].items():
                if neighbor not in visited:
                    total_time = current_time + info["time"]
                    heapq.heappush(queue, (total_time, neighbor, path))

        print("No route found between the selected airports.")


# Create the flight planner
planner = FlightRoutePlanner()

# Add real-like airport routes
planner.add_route("LHR", "AMS", 371, 80)    # London to Amsterdam
planner.add_route("LHR", "CDG", 348, 80)    # London to Paris
planner.add_route("LHR", "MUC", 943, 115)   # London to Munich
planner.add_route("AMS", "MUC", 664, 95)    # Amsterdam to Munich
planner.add_route("AMS", "DXB", 5160, 390)  # Amsterdam to Dubai
planner.add_route("CDG", "DXB", 5245, 410)  # Paris to Dubai
planner.add_route("MUC", "RUH", 4010, 330)  # Munich to Riyadh
planner.add_route("DXB", "RUH", 875, 110)   # Dubai to Riyadh
planner.add_route("RUH", "JED", 852, 95)    # Riyadh to Jeddah
planner.add_route("JED", "CAI", 1215, 130)  # Jeddah to Cairo

# Display all routes
planner.show_routes()

# Find shortest path by flight time
planner.shortest_path("LHR", "RUH")