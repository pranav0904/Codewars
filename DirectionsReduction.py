'''
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed 
(W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.

'''

def dirReduc(arr):
    directions = {"NORTH" : "SOUTH", "SOUTH" : "NORTH", "EAST":"WEST", "WEST":"EAST"}
    min_path=[]
    for dir in arr:
        if min_path and directions[dir] == min_path[-1]:
            min_path.pop()
        else:
            min_path.append(dir)
    return min_path