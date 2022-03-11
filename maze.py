import csv

with open("map_maze/rect_01.map", "r") as tf:
    lines = tf.read().split('\n')
    for line in lines:
        for column in line:
            print(column)
    

print ('bonjour')