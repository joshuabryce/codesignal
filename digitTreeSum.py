'''

We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}
the output should be
digitTreeSum(t) = 218.
There are 3 numbers encoded in this tree:

Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.
t = {
    "value": 0,
    "left": {
        "value": 9,
        "left": null,
        "right": null
    },
    "right": {
        "value": 9,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be
digitTreeSum(t) = 193.
Because 09 + 091 + 093 = 193

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers. It's guaranteed that the sum of encoded integers won't exceed 252.

Guaranteed constraints:
1 ≤ tree size ≤ 2000,
1 ≤ tree depth ≤ 9,
0 ≤ node value ≤ 9.

[output] integer64

The sum of the integers encoded in t, as described above.
[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name


Input:
t: {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}

Expected Output:
218
Click the "Run Tests" button to see output and console logs.

'''


from collections import deque

class Node:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None


def printTree(root):
    buf = deque()
    output = []
    if not root:
        print ('$')
    else:
        buf.append(root)
        count, nextCount = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.value)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print (output)
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['$']*len(buf))
        print (output)

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

t= {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 1,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 4,
        "left": None,
        "right": None
    }
}
t=obj(t)
printTree(t)
print('Expected Output: 218')

'''
dfs? recursive algorithm...

def dfs(curr,sol,visited):
    add current onto visited
    
    if current is a solution:
        add current to solutions
    for each edge from current:
        new_state <- state obtained from current by following edge
        if new_state not in visited:
            dfs(new_state,solutions,visited)

'''

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def dfs(current, visited):
    # base case
    if (current is None):
        return 0
    visited = visited * 10 + current.value
    if (current.left is None and current.right is None):
        return visited
    return (dfs(current.left, visited) + dfs(current.right, visited))
    # 103+101+14

def digitTreeSum(t):
    return dfs(t, 0)

print(digitTreeSum(t))
