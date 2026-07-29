#passing tuple to trees

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
    
def parse_tuple(data):
      if isinstance(data, tuple) and len(data) == 3:
            node = Node(data[1])
            node.left = parse_tuple(data[0])
            node.right = parse_tuple(data[2])
      elif data is None:
            return None
      else:
            node =Node(data)
      return node 

data = ((0,1,2),3,(4,5,6))
node = parse_tuple(data)
#print(node.left.right)

#traversal 
def inorder(data):
     if data is None:
          return 
     inorder(data.left)
     print(data)
     inorder(data.right)

#inorder(node)
#preorder
def preod(data):
     if data is None:
          return 

     print(data)
     preod(data.left)
     preod(data.right)
#preod(node)

#search an element

def search(data,target):
     if data is None:
          return False
     if data.value == target:
          return True
     #elif data.value < target:
       #   return search(data.right, target)
     #else:
            #return search(data.left, target)
     else:
          return search(data.right, target) or search(data.left, target)

print(search(node, 0))