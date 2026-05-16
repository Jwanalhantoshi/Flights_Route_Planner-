import networkx as nx
import matplotlib.pyplot as plt

class FlightRoutePlanner:

    def __init__(self):

        self.graph = {
            "Riyadh": {
                "Jeddah": {
                    "distance": 950,
                    "duration": "1h 40m",
                    "go": {"dep": "08:00", "arr": "09:40"},
                    "back": {"dep": "14:00", "arr": "15:40"}
                },
                "Abha": {
                    "distance": 850,
                    "duration": "1h 20m",
                    "go": {"dep": "10:00", "arr": "11:20"},
                    "back": {"dep": "16:00", "arr": "17:20"}
                }
            },

            "Jeddah": {
                "Cairo": {
                    "distance": 1200,
                    "duration": "2h",
                    "go": {"dep": "18:00", "arr": "20:00"},
                    "back": {"dep": "21:00", "arr": "23:00"}
                }
            },

            "Dammam": {
                "Doha": {
                    "distance": 390,
                    "duration": "1h",
                    "go": {"dep": "12:00", "arr": "13:00"},
                    "back": {"dep": "18:00", "arr": "19:00"}
                }
            },

            "Abha": {
                "Riyadh": {
                    "distance": 850,
                    "duration": "1h 20m",
                    "go": {"dep": "09:00", "arr": "10:20"},
                    "back": {"dep": "17:00", "arr": "18:20"}
                }
            },

            "UAE": {
                "London": {
                    "distance": 5500,
                    "duration": "7h 30m",
                    "go": {"dep": "07:00", "arr": "14:30"},
                    "back": {"dep": "16:00", "arr": "23:30"}
                }
            }
        }

    def draw_city(self, city_name):

        G = nx.DiGraph()
        table_data = []

        for dest, info in self.graph[city_name].items():

            G.add_edge(city_name, dest)

            table_data.append([
                f"{city_name} → {dest}",
                f"{info['distance']} km",
                info['duration'],
                f"{info['go']['dep']} → {info['go']['arr']}",
                f"{info['back']['dep']} → {info['back']['arr']}"
            ])

        pos = nx.spring_layout(G, seed=10, k=2.5)

        fig, ax = plt.subplots(figsize=(11, 6))

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=3000,
            font_size=11,
            font_weight="bold",
            arrows=True,
            arrowsize=18,
            ax=ax
        )

        table = plt.table(
            cellText=table_data,
            colLabels=[
                "Route",
                "Distance (km)",
                "Duration",
                "Go Time",
                "Return Time"
            ],
            loc="bottom",
            cellLoc="center"
        )

        table.scale(1, 1.5)

        plt.title(f"✈️ Flight Details - {city_name}", fontsize=14)
        plt.axis("off")
        plt.show()


planner = FlightRoutePlanner()

planner.draw_city("Riyadh")
planner.draw_city("Jeddah")
planner.draw_city("Dammam")
planner.draw_city("Abha")
planner.draw_city("UAE")