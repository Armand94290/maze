

def get_starting_finishing_points():
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
    return [0, _start[0]], [len(maze) - 1, _end[0]]


def maze_solver():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print( f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'c':
                print( f'{maze[i][j]}', end=" ")
            elif maze[i][j] == '0':
                print( f'{maze[i][j]}', end=" ")
            else:
                print(f'{maze[i][j]}', end=" ")
        print('\n')


def escape():
    current_cell = rat_path[len(rat_path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == 'c':
        maze[current_cell[0] + 1][current_cell[1]] = '0'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == 'c':
        maze[current_cell[0]][current_cell[1] + 1] = '0'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == 'c':
        maze[current_cell[0] - 1][current_cell[1]] = '0'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == 'c':
        maze[current_cell[0]][current_cell[1] - 1] = '0'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape()
    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'


if __name__ == '__main__':
    maze = [
        ['*', 'c', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*',
         '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', 'c', 'c', '*', 'c', '*', 'c', 'c', '*', '*', 'c', 'c', 'c', 'c',
         'c', '*', '*', 'c', '*', '*', 'c', 'c', 'c', 'c', 'c', 'c', '*'],
        ['*', '*', 'c', '*', 'c', 'c', 'c', '*', '*', '*', '*', '*', '*', '*',
         'c', 'c', 'c', 'c', 'c', '*', '*', '*', '*', '*', '*', 'c', '*'],
        ['*', 'c', 'c', 'c', 'c', '*', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
         'c', '*', 'c', '*', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', '*'],
        ['*', '*', '*', 'c', '*', '*', 'c', '*', 'c', '*', 'c', '*', '*', '*',
         '*', '*', '*', '*', '*', '*', '*', 'c', '*', '*', '*', 'c', '*'],
        ['*', 'c', 'c', 'c', 'c', '*', '*', '*', '*', '*', '*', '*', '*', 'c',
         'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', '*', 'c', 'c', 'c', '*'],
        ['*', 'c', '*', 'c', '*', '*', '*', '*', 'c', 'c', '*', 'c', '*', '*',
         '*', 'c', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'c', '*'],
        ['*', '*', '*', '*', '*', '*', 'c', '*', '*', 'c', 'c', 'c', '*', 'c',
         '*', '*', '*', '*', '*', '*', 'c', 'c', 'c', 'c', 'c', 'c', '*'],
        ['*', 'c', 'c', 'c', 'c', 'c', 'c', '*', '*', '*', '*', 'c', '*', 'c',
         'c', 'c', 'c', 'c', 'c', 'c', 'c', '*', 'c', '*', 'c', '*', '*'],
        ['*', '*', 'c', '*', 'c', '*', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
         '*', '*', 'c', '*', 'c', '*', 'c', '*', 'c', '*', 'c', 'c', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*',
         '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'c', '*']
    ]

    start, finish = get_starting_finishing_points()
    maze[start[0]][start[1]] = '0'

    rat_path = [start]
    escape()
    print(maze_solver())
