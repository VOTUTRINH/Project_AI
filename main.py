import os 
import DFS
import BFS
import UCS
import A_STAR
import GBFS
import UTILITY
OUTPUT='./output'
OUTPUT_LV1='./output/level_1'
OUTPUT_LV2 ='./output/level_2'
INPUT_LV1 ='./input/level_1'
INPUT_LV2='./input/level_2'
ADVANCE = './input/advance'
AlGORITHM =['bfs','dfs','ucs']

if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)
if not os.path.exists(OUTPUT_LV1):
    os.makedirs(OUTPUT_LV1)
if not os.path.exists(OUTPUT_LV2):
    os.makedirs(OUTPUT_LV2)


i=1
with os.scandir(INPUT_LV1) as level_1:
    for f in level_1:
        out_path = OUTPUT_LV1 + '/input'+str(i)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        
        for x in AlGORITHM:
            out_path_alg = out_path + '/' + x
            if not os.path.exists(out_path_alg):
                os.makedirs(out_path_alg)
    #Run alogrithm level 1 
        DFS.run_dfs(f.path,  out_path +  '/dfs')

        BFS.run_bfs(f.path,  out_path + '/' + 'bfs')

        UCS.run_ucs(f.path, out_path +'/ucs')
        
       # A_STAR.run_astar(f.path, out_path +'/'+'astar')

        A_STAR.run_astar(f.path, out_path)
        
        GBFS.run_gbfs(f.path, out_path )

        i=i+1

i=1
with os.scandir(INPUT_LV2) as level_2:
    for f in level_2:
        out_path = OUTPUT_LV2 + '/input'+str(i)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        if not os.path.exists(out_path + '/algo1'):
            os.makedirs(out_path +'/algo1')
            
        UTILITY.run_utility(f.path,out_path + '/algo1')
        i=i+1

        
        


