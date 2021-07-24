def fillMaw(seat):
    seat = []
    for i in seat:
        for j in len(seat[i]):
            seat[i][j][0] = "A"
            seat[i][j][len(seat[i][j]) - 1] = "A"
    for i in seat:
        seat[0][i][0] = "W"
        seat[len(seat) - 1][i][len(seat[len(seat) - 1][i]) - 1] = "W"
    for i in seat:
        for k in seat:
            seat[i][0][k]="M"
            seat[i][len(seat[i][k])-1][k]="M"
    for i in seat:
        print(seat[i])


def printVal(seat, col, row):
    seat=[]
    str1 = ""
    for i in row:
        for j in col:
            if seat[j] is None or seat[j][i] is None:
                str1 = "- "
                continue
            for k in seat[i][j]:
                str1 += (seat[j][i][k] + " ")
            str1 += ","
        str1 += "\n"
    for i in str1:
        print(str1[i])


def replacenum(val, count, seat, col, row):
    for i in col:
        for j in row:
            if seat[j] is None or seat[j][i] is None:
                continue
            for k in len(seat[j][i]):
                if seat[j] is not None and seat[j][i] is not None and seat[j][i][k] == val:
                    seat[j][i][k] = count
                    count += 1
    for i in seat:
        print(seat[i])
    print(count)


import numpy as np

row = np.array([])
col = np.array([])
arr = []
count = 0
seat = []

count = 0
val = ["A", "M", "W"]
seat = []
fillMaw(seat)
printVal(seat, col, row)
replacenum(val, count, seat, col, row)
