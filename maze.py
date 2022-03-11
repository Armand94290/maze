import csv

with open("map_maze/rect_01.map", "r") as map:
    lines = map.read().split('\n')
matrix = []
x = 0
for line in lines:
    y = 0
    if x == 0 or x > len(matrix) - 1:
        matrix.append([])

    for value in line:
        matrix[x].append(value)
        print(matrix[x][y])
        y += 1
        
    x += 1

for i in range (0,12):
    print(matrix[i])

