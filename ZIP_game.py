

mm=[[11,0,0,6,0,7],
    [0,0,10,0,1,0],
    [0,3,0,5,0,0],
    [9,0,4,0,0,0],
    [0,2,0,0,0,0],
    [8,0,0,0,0,0]]

mv=[[0 for _ in range(len(mm))] for _ in range(len(mm))]
r=c=0# r,c are position of starting element
start_element=1
end_element=1
for i in range(len(mm)):
    for j in range(len(mm[i])):
        if(mm[i][j]==start_element):
            r,c=i,j
        elif(mm[i][j]>end_element):
            end_element=mm[i][j]


def zip(mm,mv,r,c,st,start,end):
    # print(r,c)
    mv[r][c] = 1
    # print(22222,mm[r][c+1], start+1)

    if (r > 0 and mm[r - 1][c] == start + 1):
        zip(mm, mv, r - 1, c, st + "U", start + 1,end)
    if (c > 0 and mm[r][c - 1] == start + 1):
        zip(mm, mv, r, c - 1, st + "L", start + 1,end)
    if (r < len(mm[0]) - 1 and mm[r + 1][c] == start + 1):
        zip(mm, mv, r + 1, c, st + "D", start + 1,end)
    if (c <len(mm[0]) - 1 and mm[r][c + 1] == start + 1):
        zip(mm, mv, r, c + 1, st + "R", start + 1,end)
    if(len(st)== (len(mm[0])**2)-1):
        print(st)
        exit()
        return

    if(start==end):
        # print(st,1110)
        return
    # print(111111,mv[r + 1][c], mm[r + 1][c])
    if (r > 0 and mv[r - 1][c] != 1 and mm[r-1][c] == 0):
        zip(mm, mv, r - 1, c, st + "U", start,end)
    if (c > 0 and mv[r][c - 1] != 1 and mm[r][c - 1] == 0):
        zip(mm, mv, r, c - 1, st + "L", start,end)
    if (r < len(mm[0]) - 1 and mv[r + 1][c] != 1 and mm[r + 1][c] == 0):
        zip(mm, mv, r + 1, c, st + "D", start,end)
    if (c < len(mm[0]) - 1 and mv[r][c + 1] != 1 and mm[r][c + 1] == 0):
        zip(mm, mv, r, c + 1, st + "R", start,end)
    mv[r][c]=0

zip(mm,mv,r,c,"",start_element,end_element)


