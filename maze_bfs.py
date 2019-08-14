import numpy as np 

############ bfs ###############
def bfs(map):

    #### 上下左右四个方向的增量 #####
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    #### 节点列表 #####
    nodes=[]
    nodes.append((0,1,0))

    #### 节点访问表——记录节点是否被访问 #####
    node_visit=np.array([[0]*10]*10)
    node_visit[0][1]=1

    #### bfs过程 #####
    while len(nodes)!=0:
        
        #### 从节点列表输出一个节点 #####
            node=nodes[0]

        #### 上下左右四个方向遍历 #####
        for i in range(0,4):
            
            #### 上下左右四个方向遍历 #####
            x=node[0]+dx[i]
            y=node[1]+dy[i]

            #### 步数 #####
            step=node[2]

            #### 判断是否到达终点 #####
            if x==9 and y==8:
               return step+1

            #### 判断节点是否符合条件 #####
            if x>=1 and x<=9 and y>=1 and y<=9 and node_visit[x][y]==0 and map[x][y]==1:

               #### 将节点压入节点列表nodes，说明进入下一层，step+1 #####
               nodes.append((x,y,step+1))

               #### 该节点标记为已经访问过 #####
               node_visit[x][y]=1

        #### 从节点列表移除上一层的节点 #####
        del(nodes[0])

    #### 如果没有路径，则表明迷宫无法走出 #####
    return 0


if __name__ == '__main__':
    
    
    
    map=np.array([[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0]
        ,[0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,0]
        ,[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0]
        ,[0,0,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,0]
        ,[0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,0]])


    map=np.array([[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0]
    ,[0,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,0]
    ,[0,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,0]
    ,[0,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,0]
    ,[0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,1,0]])

    res=bfs(map)
    print(res)

