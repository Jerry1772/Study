# https://school.programmers.co.kr/learn/courses/30/lessons/42628
from typing import Tuple

class Node:
    def __init__(self, data):
        self.value = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root=None
    
    def I(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self.cur_node = self.root
            
        while True:
            if value < self.cur_node.value:
                if self.cur_node.left != None:
                    self.cur_node = self.cur_node.left
                else:
                    self.cur_node.left = Node(value)
                    break
            else:
                if self.cur_node.right != None:
                    self.cur_node = self.cur_node.right
                else:
                    self.cur_node.right = Node(value)
                    break
    
    def search_node(self, search_type:int) -> Tuple[Node,Node]:
        """
        input: search_type: 1(max) or -1(min)
        
        output: Parent Node, Min/Max Node
        if Node not exists, None
        """
        self.cur_node = self.root
        if self.root is None:
            return None,None
        if search_type == 1:
            if self.cur_node.right is None:
                return None, self.cur_node
            while self.cur_node.right.right != None:
                self.cur_node = self.cur_node.right
            return self.cur_node, self.cur_node.right
        else:
            if self.cur_node.left is None:
                return None, self.cur_node
            while self.cur_node.left.left != None:
                self.cur_node = self.cur_node.left
            return self.cur_node, self.cur_node.left
        
    def D(self, search_type:int):
        self.par_node, self.cur_node = self.search_node(search_type)
        if self.cur_node is None:
            return
        if search_type == 1:
            if self.par_node is None:
                self.root = self.cur_node.left
            else:
                self.par_node.right = self.cur_node.left
        else:
            if self.par_node is None:
                self.root = self.cur_node.right
            else:
                self.par_node.left = self.cur_node.right
    
    def result(self):
        if self.root is None:
            return [0, 0]
        else:
            return [self.search_node(1)[1].value, self.search_node(-1)[1].value]
                
                
            
def solution(operations):
    t = Tree()
    for op in operations:
        ops = op.split(' ')
        getattr(t,ops[0])(int(ops[1]))
    return t.result()

if __name__ == "__main__":
    param = {
        "operations": ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    }
    result = [333, -45]
    print(solution(**param), result)