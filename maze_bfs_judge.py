# -*- coding: utf-8 -*-
import numpy as np 

############ bfs ###############
def bfs(map, n, m, t):
    
    #### 寻找起点和终点 #####
    for i in range(0,m):
        for j in range(0,n):
            if map[i][j]==2:
                start=(i,j)
            if map[i][j]==3:
                end=(i,j)

    #### 上下左右四个方向的增量 #####
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    #### 当前节点列表 #####
    nodes_cur=[]
    nodes_cur.append(start)
    
    #### 下一层节点列表 #####
    nodes_next=[]

    #### 节点访问表——记录节点是否被访问 #####
    node_visit=np.array([[0]*n]*m)
    node_visit[start[0]][start[1]]=1

    #### bfs过程 #####
    while len(nodes_cur)!=0:
        
        #### 从当前层节点列表输出一个节点 #####
        node=nodes_cur[0]

        #### 上下左右四个方向遍历 #####
        for i in range(0,4):

            #### 上下左右四个方向遍历 #####
            x=node[0]+dx[i]
            y=node[1]+dy[i]


            #### 判断是否到达终点 #####
            if x==end[0] and y==end[1]:
               return 'yes'

            #### 判断节点是否符合条件 #####
            if x>=0 and x<m and y>=0 and y<n and node_visit[x][y]==0 and map[x][y]==1:

               #### 将节点压入下一层的节点列表nodes_next #####
               nodes_next.append((x,y))

               #### 该节点标记为已经访问过 #####
               node_visit[x][y]=1

        #### 从节点列表移除当前层的节点 #####
        del(nodes_cur[0])
        
        #### 当前层处理完 #####
        if len(nodes_cur)==0:
            
            #### 剩下的时间-1 #####
            t=t-1
            
            #### 时间用完 #####
            if t<0:
                return 'no'
            
            #### 处理下一层 #####
            else:
                nodes_cur=nodes_next.copy()
                nodes_next=[]

    #### 如果没有路径，则表明迷宫无法走出 #####
    return 'no'


if __name__ == '__main__':
    
    #### 迷宫 #####
    map=np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[2,0,0,3]])
    
    #### 列数，行数，天数 #####
    n=4
    m=4
    t=10
    
    #### bfs #####
    res=bfs(map, n, m, t)
    print(res)

