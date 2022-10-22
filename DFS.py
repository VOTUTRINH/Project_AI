import matplotlib.pyplot as plt
import os
import readFile as rf
import drawMap as dm


def dfs(maze,start,goal):
    stack=[]
    stack.append(start)
    visited =[]
    path =[]
    parent_map ={}
    cost =0
    while(stack):

        cur_point=stack.pop()
        visited.append(cur_point)
        
        if cur_point == goal:
            path.append(cur_point)
            while(path[-1] in parent_map):
                path.append(parent_map[path[-1]])
            cost = len(path) - 1 
            return path[::-1],cost

        near_point =rf.findNearPoint(cur_point,maze)

        for i in near_point:
            if i in visited:
                continue
            if i in stack: 
                stack.remove(i)
            stack.append(i)
            parent_map[i]=cur_point
            

    return path,len(path)-1



def run_dfs(file_path_in,file_path_out):

    bonus,maze= rf.read_file(file_path_in)

    start = rf.findStartPoint('S',maze)
    goal = rf.findEndPoint(maze)

    path,cost = dfs(maze,start,goal)


    plt= dm.visualize_maze(maze,bonus,start,goal,path)

    sample_file_name = "dfs.jpg"
    plt.savefig(file_path_out + '/' +sample_file_name)

    f = open(file_path_out + '/dfs.txt', "w")
    if cost < 0:
        f.write('NO')
    else:
        f.write(str(cost))
    f.close()

   






