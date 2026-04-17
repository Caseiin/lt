#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    # i=1 Skips the first column as it contains only the Course however first bug: index does not enumerate
    for i, head in enumerate(headings): #counts throw the column
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    #best = best_idx =  0 Second bug is best_idx is never updates and set to the current student number
    best = 0
    best_idx = None

    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        if mark > best:
            best=mark
            best_idx = data[num_col] # tracks the student number
    return best_idx, best

f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))
