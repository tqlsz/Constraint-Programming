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
        self.color = 0


class Graph():
    '''图类'''
    '''初始化图类，顶点'''
    def __init__(self):
        self.neighbors_nodes = {}

    def add_node(self, node):
        self.neighbors_nodes[node] = []

    def add_nodes(self, nodes):
        for node in nodes:
            if node not in self.neighbors_nodes:
                self.neighbors_nodes[node] = []

    def print_graph(self):
        for (key, value) in self.neighbors_nodes.iteritems():
            print key.el, [el.el for el in value]

    def add_edge(self, edge):
        u, v = edge
        if v not in self.neighbors_nodes[u]:
            self.neighbors_nodes[u].append(v)
            if u not in self.neighbors_nodes[v]:
                self.neighbors_nodes[v].append(u)

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
    # graph1.depth_first_search()
    path, all_path = [], []
    # graph1.breath_first_search(nodes[0])
    graph1.find_path(nodes[7], nodes[6], path, all_path)
    for path in all_path:
        print [node.el for node in path]
