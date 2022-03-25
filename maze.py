from asyncio.windows_events import NULL
import math
from operator import indexOf
from simpleai.search import SearchProblem, astar


class MazeSolver(SearchProblem):
    def __init__(self, tableau):
        self.tableau = tableau
        self.goal = (0, 0)

        for y in range(len(self.tableau)):
            for x in range(len(self.tableau[y])):
                if self.tableau[y][x] == "1":
                    self.initial = (x, y)
                elif self.tableau[y][x] == "2":
                    self.goal = (x, y)

        super(MazeSolver, self).__init__(initial_state=self.initial)

    def actions(self, state):
        moves = []
        for move in COSTS.keys():
            newx, newy = self.result(state, move)
            if self.tableau[newy][newx] != "*":
                moves.append(move)

        return moves

    def result(self, state, move):
        x, y = state

        if move.count("up"):
            y -= 1
        if move.count("down"):
            y += 1
        if move.count("left"):
            x -= 1
        if move.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, move, state2):
        return COSTS[move]

    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal

        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


with open("map_maze/oval_01.map", "r") as map:
    lines = map.read()

if __name__ == "__main__":
    MAP = lines

    MAP = [list(x) for x in MAP.split("\n") if x]

    cost_move = 1.0

    COSTS = {
        "up": cost_move,
        "down": cost_move,
        "left": cost_move,
        "right": cost_move,
    }

    problem = MazeSolver(MAP)

    result = astar(problem, graph_search=True)

    path = [x[1] for x in result.path()]

    print()
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) == problem.initial:
                print('1', end='')
            elif (x, y) == problem.goal:
                print('2', end='')
            elif (x, y) in path:
                print('0', end='')
            else:
                print(MAP[y][x], end='')

        print()
