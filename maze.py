import csv
from tracemalloc import start
from turtle import st

with open("map_maze/rect_01.map", "r") as map:
    lines = map.read().split('\n')
matrix = []

start_x = 0
start_y = 0
end_x = 0
end_y = 0

for line in lines:
    y = 0
    x = 0
    if x == 0 or x > len(matrix) - 1:
        matrix.append([])
    for value in line:
        if value == '1':
            start_x = x
            start_y = y

        if value == '2':
            end_x = x
            end_y = y

        matrix[x].append(value)
        y += 1
        
    x += 1


# def createmaze():
#     maze = []
#     for i in range (0,x):
#         maze.append(matrix[i])
#     print (maze)
#     return maze

def get_starting_finishing_points():
    _start = [i for i in range(len(maze[1])) if maze[start_x][start_y] == '1']
    _end = [i for i in range(len(maze[end_x])) if maze[end_x][end_y] == '2']
    return [start_x, _start[0]], [end_x, _end[0]]


def maze_solver():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == ' ':
                print(f'{maze[i][j]}', end=" ")
            elif maze[i][j] == ' ':
                print(f'{maze[i][j]}', end=" ")
            elif maze[i][j] == '0':
                print(f'{maze[i][j]}', end=" ")
            else:
                print(f'{maze[i][j]}', end=" ")
        print('\n')


def escape():
    current_cell = rat_path

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == ' ':
        maze[current_cell[0] + 1][current_cell[1]] = '0'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == ' ':
        maze[current_cell[0]][current_cell[1] + 1] = '0'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == ' ':
        maze[current_cell[0] - 1][current_cell[1]] = '0'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == ' ':
        maze[current_cell[0]][current_cell[1] - 1] = '0'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape()

    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = ' '


if __name__ == '__main__':
    maze = [
        ['*','*','*','*','*','*','*','*','*','*','*','*','*'],
        ['*',' ',' ','*','*',' ',' ',' ',' ',' ',' ',' ','1'],
        ['*',' ',' ',' ',' ',' ','*','*','*','*','*','*','*'],
        ['*',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*'],
        ['*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
        ['*',' ',' ',' ',' ',' ','*','*','*','*',' ','*','*'],
        ['*','*','*','*','*','*','*','*','*','*',' ','*','*'],
        ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
        ['*',' ',' ',' ',' ','*','*','*','*','*','*','*','*'],
        ['*',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ','*'],
        ['*','*','*','*','*','*','*','*',' ',' ',' ',' ','*'],
        ['*','*','*','*','*','*','*','*','*','2','*','*','*']
    ]
    print (maze[1][12])

    start, finish = get_starting_finishing_points()
    maze[start[0]][start[1]] = '0'

    rat_path = [start]
    escape()
    print(maze_solver())
