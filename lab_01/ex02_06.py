input_str = input("nhập X,Y:")
demensions=[int(X) for X in input_str.split(',')]
rowNum=demensions[0]
colNum=demensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col
        print(multilist)