class Node(object):
    def __init__(self,val):
        self.val = val
    
    def __eq__(self,other):
        return self.val == other.val


    def __hash__(self):
        return hash(self.val)


s = set()
n1 = Node(val = 1)
n2 = Node(val = 2)
n3 = Node(val = 1)
n4 = Node(val = 2)

s.add(n1)
s.add(n2)
s.add(n3)

print('hello world',n4 in list(s))

