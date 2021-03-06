import sys
from math import sin, cos, radians

dat = [[x.strip('\n')[0], int(x.strip('\n')[1:])] for x in sys.stdin]

Wx, Wy = 10, 1
x,y = 0,0

def COS(N):
    return(round(cos(radians(N)),0))

def SIN(N):
    return(round(sin(radians(N)),0))

for arg in dat:
    # forward moves towards waypoint
    if arg[0] == 'F':
        y += Wy*arg[1]
        x += Wx*arg[1]

    # lefts and rights rotate waypoint around ship
    if arg[0] == "R":
        tX = Wx
        tY = Wy
        Wx = COS(arg[1])*tX + SIN(arg[1])*tY
        Wy = COS(arg[1])*tY - SIN(arg[1])*tX
    if arg[0] == "L":
        tX = Wx
        tY = Wy
        Wx = COS(arg[1])*tX - SIN(arg[1])*tY
        Wy = COS(arg[1])*tY + SIN(arg[1])*tX

    # cardinal directions omve waypoints
    if arg[0] == 'N':
        Wy += arg[1]
    if arg[0] == 'S':
        Wy -= arg[1]
    if arg[0] == 'E':
        Wx += arg[1]
    if arg[0] == 'W':
        Wx -= arg[1]
print(abs(x)+abs(y))
