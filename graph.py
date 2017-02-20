# coding:utf-8
import copy

'''用字典表示图'''
graph = {'a': ['b', 'c'],
         'b': ['c', 'd', 'e', 'f'],
         'c': ['a', 'd', 'f'],
         'd': ['c'],
         'e': ['d', 'f'],
         'f': ['c']}

'''找一个路径'''


def find_path(graph, start, end, path, all_path):
    '''开始节点必须是个key'''
    path.append(start)
    # path = path + [start]
    if start == end:
        all_path.append(copy.deepcopy(path))
        path.pop()
        return path
    if start not in graph:
        path.pop()
        return None
    '''使用深度优先搜索'''
    for el in graph[start]:
        print path
        if el not in path:
            find_path(graph, el, end, path, all_path)
    path.pop()


def test(graph):
    path, all_path = [], []
    find_path(graph, 'a', 'f', path, all_path)
    print all_path


class Node():
    '''结点类'''
    def __init__(self, el=0):
        self.el = el
        self.color = -1


class Graph():
    '''图类'''
    '''初始化图类，顶点'''
    def __init__(self):
        self.neighbors_nodes = {}
        self.nodes = []
        '''已经使用的颜色个数'''
        self.color_all = 0
        '''已经着色的节点数'''
        self.node_color_num = 0
        self.color_did = []
        self.color_min = 10000

    def get_nodes_len(self):
        return len(self.nodes)

    def add_node(self, node):
        self.neighbors_nodes[node] = []
        self.nodes.append(node)

    def add_nodes(self, nodes):
        for node in nodes:
            if node not in self.neighbors_nodes:
                self.neighbors_nodes[node] = []
                self.nodes.append(node)

    def print_graph(self):
        for (key, value) in self.neighbors_nodes.iteritems():
            print key.el, [el.el for el in value]

    def add_edge(self, edge):
        u, v = edge
        if v not in self.neighbors_nodes[u]:
            self.neighbors_nodes[u].append(v)
            if u not in self.neighbors_nodes[v]:
                self.neighbors_nodes[v].append(u)
        self.sort_dic = sorted(self.neighbors_nodes.iteritems(), key=lambda asd: len(asd[1]), reverse=True)

    def depth_first_search(self, root=None):
        '''从root结点深度优先遍历图'''
        def dfs(node):
            if node.color == 1:
                return
            node.color = 1
            print node.el
            for value in self.neighbors_nodes[node]:
                dfs(value)
        if root:
            dfs(root)

        for node in self.neighbors_nodes:
            if node.color == 0:
                dfs(node)

    def breath_first_search(self, root=None):
        '''从root结点广度优先遍历图'''
        def bfs(node):
            if node.color == 1:
                return
            queue = [node]
            while queue:
                temp_node = queue.pop(0)
                temp_node.color = 1
                print temp_node.el
                for value in self.neighbors_nodes[temp_node]:
                    if value.color == 0 and value not in queue:
                        queue.append(value)

        if root:
            bfs(root)

        for node in self.neighbors_nodes:
            if node.color == 0:
                bfs(node)

    def find_path(self, start_node, end_node, path, all_path):
        '''start_node是个key,path保存路径，all_path保存所有路径'''
        if start_node not in self.neighbors_nodes:
            return None
        path.append(start_node)
        if start_node == end_node:
            '''到了结尾'''
            all_path.append(copy.deepcopy(path))
        else:
            for temp_node in self.neighbors_nodes[start_node]:
                if temp_node not in path:
                    self.find_path(temp_node, end_node, path, all_path)
                    path.pop()

    def dfs_color(self, root):
        '''root可以着色方案有color_all种'''
        node_color_num = self.node_color_num
        for color in range(self.color_all+1):
            b_color = True
            if color != self.color_all:
                for temp_node in self.neighbors_nodes[root]:
                    '''通过root相邻节点的着色，判断color是否合适'''
                    if temp_node.color == color:
                        b_color = False
                        break
            else:
                self.color_all += 1
            if b_color:
                '''说明颜色符合要求'''
                root.color = color
                self.node_color_num += 1
                if self.color_all >= self.color_min:
                    return
                if self.node_color_num == self.get_nodes_len():
                    '''说明已经全部着色'''
                    self.color_min = self.color_all
                    self.color_did = [node.color for node in self.nodes]
                    return
                else:
                    '''对邻节点进行着色'''
                    for temp_node in self.neighbors_nodes[root]:
                        if temp_node.color == -1:
                            self.dfs_color(temp_node)
                            temp_node.color = -1
            self.node_color_num = node_color_num

    def color_by_dfs(self, i=0, temp_color_all=0):
        '''遍历节点'''
        temp_color_all
        for color in range(temp_color_all+1):
            b_color = True
            '''判断颜色是否符合要求'''
            if color != temp_color_all:
                for node in self.neighbors_nodes[self.nodes[i]]:
                    if node.el-1 < i and node.color == color:
                        b_color = False
                        break
            else:
                temp_color_all += 1
            if b_color:
                '''说明颜色符合要求'''
                # print i, temp_color_all
                if temp_color_all >= self.color_min:
                    return False
                self.nodes[i].color = color
                if i == self.get_nodes_len()-1:
                    self.color_min = temp_color_all
                    self.color_did = [node.color for node in self.nodes]
                    print self.color_min
                    '''着色完毕'''
                    return True
                else:
                    self.color_by_dfs(i+1, temp_color_all)
            # self.color_all = temp_color_all

    def color_by_geedy(self, i=0):
        '''贪心算法:使用一种颜色对尽可能多节点着色'''
        for node in self.sort_dic:
            if node[0].color != -1:
                continue
            b_color = True
            for temp_node in node[1]:
                if temp_node.color == i:
                    b_color = False
                    break
            if b_color:
                node[0].color = i
                self.node_color_num += 1
                if self.node_color_num == self.get_nodes_len():
                    self.color_did = [node.color for node in self.nodes]
                    self.color_min = i+1
                    return
        self.color_by_geedy(i+1)


if __name__ == '__main__':
    # test(graph)
    graph1 = Graph()
    nodes = [Node(i+1) for i in range(10)]
    graph1.add_nodes(nodes)
    graph1.add_edge((nodes[0], nodes[1]))
    graph1.add_edge((nodes[0], nodes[2]))
    graph1.add_edge((nodes[0], nodes[4]))
    graph1.add_edge((nodes[1], nodes[3]))
    graph1.add_edge((nodes[1], nodes[4]))
    graph1.add_edge((nodes[3], nodes[7]))
    graph1.add_edge((nodes[4], nodes[7]))
    graph1.add_edge((nodes[2], nodes[5]))
    graph1.add_edge((nodes[2], nodes[6]))
    graph1.add_edge((nodes[5], nodes[6]))
    graph1.add_edge((nodes[8], nodes[9]))
    # graph1.print_graph()

    graph1.color_by_geedy(0)
    # graph1.color_by_dfs(0, 0)
    print graph1.color_min
    print graph1.color_did
    # graph1.print_graph()
    # graph1.depth_first_search()
