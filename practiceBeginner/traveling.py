n = int(input())
points = [[0,0,0]]
for i in range(n):
    t, x, y = list(map(int, input().split()))
    points.append([t, x, y])
possible = False
for i in range(n):
    steps = points[i+1][0] - points[i][0]
    #次点に最短距離で到達し、偶数steps余っているならOK。
    #到達できない、奇数しか余ってないならNG
    xDis = abs(points[i+1][1] - points[i][1])
    yDis = abs(points[i+1][2] - points[i][2])
    totalDis = xDis + yDis
    sub = steps - totalDis
    # print('sub:' + str(sub))
    if sub == 0:
        possible = True
    elif sub > 0 and sub%2 == 0:
        possible = True
    else:
        possible = False
        # print(points[i])
        break
if possible:
    print('Yes')
else:
    print('No')
