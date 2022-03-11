import csv
from tracemalloc import start
from turtle import st

with open("map_maze/rect_01.map", "r") as map:
    lines = map.read().split('\n')
matrix = []

pt_start = (0,0)
pt_finish = (0,0)
x = 0

start_x = 0
start_y = 0
end_x = 0
end_y = 0

for line in lines:
    y = 0
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

for i in range (0,12):
    print(matrix[i])

pt_start = (start_x, start_y)
print (pt_start)

