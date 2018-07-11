走迷宫最短路径采用BFS算法
=======================
# 一. 问题
> 输入一组10 x 10的数据，由#和.组成的迷宫，其中#代表墙，.代表通路，入口在第一行第二列，出口在最后一行第九列，从任意一个.都能一步走到上下左右四个方向的.，请求出从入口到出口最短需要几步？

> 输入例子

```python
#.########
#........#
#........#
#........#
#........#
#........#
#........#
#........#
#........#
########.#
结果为：16

#.########
#........#
########.#
#........#
#.########
#........#
########.#
#........#
#.######.#
########.#
结果为：30
```
# 二. 解决方法

> 因为题意是使用最少的步数走出迷宫，所要可以使用广度优先遍历的方式，每处理完一层说明走了一步，最先到达出口使用的步数最少。根据输入的例子，迷宫的走法如图1所示。 
![image](https://github.com/872822645/danxuankuangDemo/blob/master/1.jpg)

> 代码如下：

```python
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

        #### 上下左右四个方向遍历 #####
        for i in range(0,4):

            #### 从节点列表输出一个节点 #####
            node=nodes[0]

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

```
