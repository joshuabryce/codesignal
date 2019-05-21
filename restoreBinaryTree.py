#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
'''
preorder starts with root node.. mark this...

algorithm:
1. pick element from preorder and increment index preIndex for next recursive call
2. create tree with picked element
3. find index of element in inorder called inIndex
4. call build tree left
5. call build tree right
6. return

'''

class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def restoreBinaryTree(inorder, preorder):
    preIndex=0
    inIndex=0
    return buildTree(inorder, preorder,preIndex,inIndex)

def buildTree(inorder, preorder,preIndex,inIndex):
    #nodeT = Tree(preorder[preIndex])
    nodeT = Tree(preorder[0])
    preIndex+=1
    inIndex = search(inorder, nodeT.value)
    rightIndex = search(preorder, inorder[0])

    leftInOrder = []
    rightInOrder = []
    if(inIndex is not None):

        for i in range(0, inIndex):
            leftInOrder.append(inorder[i])

        for i in range(inIndex+1, len(preorder)):
            rightInOrder.append(inorder[i])

        leftpreorder = []
        rightpreorder = []

        for i in range(1, rightIndex+1):
            leftpreorder.append(preorder[i])
        for i in range(rightIndex+1, len(preorder)):
            rightpreorder.append(preorder[i])

        # left
        if(len(leftpreorder)>0):
            nodeT.left=buildTree(leftInOrder, leftpreorder,preIndex,inIndex)
        # right
        if (len(rightpreorder)>0):
            nodeT.right=buildTree(rightInOrder, rightpreorder,preIndex,inIndex)

    return nodeT

def search(t,v):
    for i in range(0,len(t)):
        if (t[i]==v):
            return i

def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level

inorder= [4, 2, 1, 5, 3, 6]
preorder= [1, 2, 4, 3, 5, 6]

t=(restoreBinaryTree(inorder, preorder))
traverse(t)