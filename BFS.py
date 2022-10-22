import drawMap as dm
import readFile as rf
import os
from inspect import BoundArguments
import queue


def bfs(u, v, matrix,used,trace):
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]
    cnt = 0
    cnt += 1
    used[u][v]=1
    h = queue.Queue()
    h.put(u)
    h.put(v)
    while h.qsize()!=0  :
        uu=h.get()
        vv=h.get()
        for i in range(4):
            if (uu + dx[i] >= 0) and (uu + dx[i] < len(matrix)) and (vv + dy[i] >= 0) and (vv + dy[i] < len(matrix[0])): 
                u1 = uu + dx[i]
                v1 = vv + dy[i]
                if (used[u1][v1] == 0) and (matrix[u1][v1] != 'x'):
                    h.put(u1)
                    h.put(v1)
                    cnt+=1
                    used[u1][v1] = used[uu][vv] + 1
                    trace[u1][v1] = i
    
    return cnt


def makearray2D(matrix):
    arr = []
    for i in range(len(matrix)):
        arr.append([])
        for  j in range(len(matrix[0])):
            arr[i].append(0)      
    return arr

def tracee(start, end,trace):
    xx = end[0] 
    yy = end[1] 
    route = []
    route.append((xx, yy))
    while (xx != start[0] or yy !=start[1]):
        if(trace[xx][yy] == 0):
            xx = xx + 1
        elif (trace[xx][yy] == 1):
            xx = xx - 1
        elif (trace[xx][yy] == 2):
            yy = yy + 1
        else:
            yy = yy - 1
        route.append((xx, yy))
    return route
    

def run_bfs(file_path_in,file_path_out):
    bonus_points, matrix = rf.read_file(file_path_in)
    s = matrix
    start = rf.findStartPoint('S',matrix)
    end = rf.findEndPoint(s)
    used = makearray2D(matrix)
    trace = makearray2D(matrix)

    cnt = bfs(start[0], start[1], matrix,used,trace)
    
    route = []
    route = tracee(start, end,trace)
    route.reverse()
   
    
    plt = dm.visualize_maze(matrix,bonus_points,start,end, route)
    sample_file_name = "bfs.jpg"
    plt.savefig(file_path_out + '/' +sample_file_name)

    f = open(file_path_out + '/bfs.txt', "w")
    if used[end[0]][end[1]] - 1 < 0:
        f.write('NO')
    else:
        f.write(str(used[end[0]][end[1]] - 1))
    f.close()

    print("---------bfs---------")
    print("Chi phi",str(used[end[0]][end[1]] - 1))
    print("So nut mo:",cnt)

    







