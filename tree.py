class Tree:
    '''
    Generic Tree Class
    '''
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return str(self.name)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    
