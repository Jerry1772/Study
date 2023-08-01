class Node:
    
    nodemap = []

    def __init__(self, data, row, col):
        self.data = data
        self.coord = (row, col)
        self.childs = []

        
    def visit(self):
        print(self.data)

    

def dfs(A:Node):
    stack = []
    visited = set()
    stack.append(A)

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        node.visit()
        stack.extend(node.childs)


if __name__ == "__main__":
    t_row, t_col = 4,6
    sMap = [101111,101010,101011,111011]
    t_map = list(map(list, list(map(str, sMap))))
    
    a = Node(1,1,1)
    Node.nodemap = t_map
    b = Node(2,2,2)


    