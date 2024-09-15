from dataclasses import dataclass
from datetime import datetime


@dataclass
class Route:
    id: int
    origin: str
    destination: str
    time: datetime


class RoutesRepoIterator:
    def __init__(self, routes, index) -> None:
        self.routes = routes
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.routes):
            raise StopIteration
        self.index += 1
        return self.routes[self.index - 1]


class RoutesRepo:
    def __init__(self):
        self.routes = [
            Route(1, "New York City", "Boston", datetime.now()),
            Route(2, "Los Angeles", "San Francisco", datetime.now()),
            Route(3, "San Diego", "Los Angeles", datetime.now())
        ]

    def __iter__(self):
        return RoutesRepoIterator(self.routes, 0)


repo = RoutesRepo()

for route in repo:
    print(route)
