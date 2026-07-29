'''
Consider the problem below
As a senior engineer at google, you are tasked with developing a fast in-memory
 data structure to manage profile information(username, name and email) for100 million users.
 it should allow the following operation to be performed efficiently

 1- Insert the profile information for a new user
 2- Find the profile information of a user, given their username
 3- Update the profile information of a user, give their username
 4- List all the users of the platform, sorted by username

 you can assume that usernames are unique 

'''
# Solution
# this is a brute force approach

class User:
      def __init__(self, username, name, email):
            self.name = name 
            self.username = username
            self.email = email

      def __repr__(self):
            return "User(username='{}', name='{}') ".format(self.username, self.name)
      def __str__(self):
            return self.__repr__()


#sample of inputs 


class UserDatabase:
    def __init__(self):
            self.users = []
    def insert(self, user):
          i = 0
          while i< len(self.users):
                if self.users[i].username > user.username:
                      break
                i +=1
          self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
              if user.username == username:
                    return user

    def update(self,user):
          target = self.find(user.username)
          target.name, target.email = user.name, user.email

    def list_all(self):
          return self.users


user1 = User('feujio','dong','dongmo18')
user2 = User('youyou','ituka','youyou18')
user3 = User('farel','urbain','farel18')
user4 = User('zez','goat','goat18')

users = [user1,user2,user3,user4]

db = UserDatabase()
for user in users:
    db.insert(user)
#print(db.list_all())

#print(db.find('feujio'))




## LET'S FIND AN OPTIMAL SOLUTION NOW 
# using binary tree:  

#question 1
#Implement a binary tree using python, and show its usage with some examples

class TreeNode:
      def __init__(self,key):
            self.key = key
            self.left = None
            self.right = None

      def __repr__(self):
            return f"key: {self.key}"
      def __str__(self):
            return self.__repr__()

node0 = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(6)
node0.left = node1
node0.right = node2
tree = node0
#print(tree.left.key)
#print(tree.right.key)


#Another tree structure
# we will be calling the root node the tree

class Treenode:
      def __init__(self,key):
            self.key = key
            self.left = None
            self.right = None
# Doing this is very expensive and time consuming
tree = Treenode(2)
m0 = Treenode(3)
m1 = Treenode(5)
l0 = Treenode(1)
m2 = Treenode(3)
m3 = Treenode(7)
l1 = Treenode(4)
l2 = Treenode(6)
l3  = Treenode(8)

tree.left = m0
tree.right = m1
m0.left = l0
m1.left = m2
m1.right = m3
m2.right = l1
m3.left = l2
m3.right = l3

#print(m1.right.key)



#Now we will use tuple to do this, which is faster and quicker
# we will create thesame tree in an easy and fast way

tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))

def parse_tuple(data):
      if isinstance(data, tuple) and len(data) == 3:
            node = Treenode(data[1])
            node.left = parse_tuple(data[0])
            node.right = parse_tuple(data[2])
      elif data is None:
            return None
      else:
            node =Treenode(data)
      return node 

# this function help us display the all the keys

def display_keys(node, space='\t', level = 0):
      if node is None:
            print(space*level + '*')
            return
      if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return 

      display_keys(node.right, space, level+1)
      print(space*level + str(node.key))
      display_keys(node.left, space, level+1)

value = parse_tuple(tree_tuple)
#print(value.left.left.key)
display_keys(value)

# Now, binary questions
# 1 Binary tree traversal questions
# we have three types of traversal
# INRODER, PREORDER, AND POSTORDER traversal

#INORDER:
# traverse the left subtree recursively inorder, then traverse the current node, then traverse the right subtree recursively inorder
#PREORRDER:
# traverse the current node, then traverse the left subtree recursively preorder, the traverse the right subtree recurlively preorder

def tranverse_in_order(node):
      if node is None:
            return []
      return (tranverse_in_order(node.left)+ [node.key]+ tranverse_in_order(node.right))


def max_height(node):
      pass 











### SOME BASICS ABOUT TREES
class TreeNode:
      def __init__(self,value,left=None,right=None):
            self.value = value
            self.left = left
            self.right = right

      def __str__(self):
            return str(self.value)

a = TreeNode(1)    
b = TreeNode(2)  
c = TreeNode(3)  
d = TreeNode(4)  
e = TreeNode(5)  
f = TreeNode(10)     
a.left = b
a.right = c
b.left = d
d.right = e
c.left = f

#this is DFS TECHNICS
#now let's do an pre order traversal
def preorder(node):
      if not node:
            return 
      print(node)
      preorder(node.left)
      preorder(node.right)

#preorder(a)

def inorder(node):
      if not node:
            return 
      inorder(node.left)
      print(node)
      inorder(node.right)
#inorder(a)

def postorder(node):
      if not node:
            return 
      postorder(node.left)
      postorder(node.right)
      print(node)
      
#postorder(a)
print("----")
#Iterative pre order traversal DFS 
def pre_order_iterative(node):
      stk = [node]

      while stk:
            node = stk.pop()
            print(node)
            if node.right: 
                  stk.append(node.right)
            if node.left:
                  stk.append(node.left)
#pre_order_iterative(a)


#BFS TECHNICS 
from collections import deque

def level_order(node):
      if node is None:
            return 
      q = deque()
      q.append(node)

      while q:
            node = q.popleft()
            print(node)
            if node.left: q.append(node.left)
            if node.right : q.append(node.right)

#level_order(a)

#Searching in a DFS

def search(node,target):
      if node is None:
            return False
      if node.value == target:
            return True

      return search(node.left, target) or search(node.right,target) 

#print(search(a,89))

## I AM CREATING A BINARY SEARCH TREE TO DO SOME FUN STUFF

class BSTN:
      def __init__(self,value,left = None, right=None):
            self.value = value
            self.left = left
            self.right = right

      def __str__(self):
            return str(self.value)

# this is my binary search Tree
#         5
#      1    8
# #  -1 3  7  9
a = BSTN(5)  
b = BSTN(1)  
c = BSTN(8)  
d = BSTN(-1)  
e = BSTN(3)  
f = BSTN(7)  
g = BSTN(9)  

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right  = g

def BStraverPre(node):
      if node is None:
            return 
      print(node)
      BStraverPre(node.left)
      BStraverPre(node.right)
#BStraverPre(a)
#print(" ----------------------")
def BStraverIno(node):
      if node is None:
            return 
      BStraverIno(node.left)
      print(node)
      BStraverIno(node.right)
#BStraverIno(a)
      
#searching in a Binary search tree has a time complexity of logn and space

def findInBST(node,target):
      if node is None:
            return False
      if node.value == target:
            return True
      if node.value < target:
            return findInBST(node.right, target)
      else:
            return findInBST(node.left, target)

print(findInBST(a,51))