print('hello world')
'''
n=1
[3,1,4,2]

[1,0,0,0]
[0,0,1,0]
[0,0,0,0]
[0,0,0,0]
'''

def isValid(b):
    #horizontal, vertical, diagonal
    for i in range(0,len(b)):
        for j in range(i+1,len(b)): #inner loop doesn't repeat from outer loop
            if(b[i]!=0 and b[j]!=0): #and b[i]!=b[j]): #unecessary with added part to second loop
                z=b[i]
                x=b[j]
                # if(i==1 and j==2):
                #     print('test')
                #hor doesn't need to be checked
                #vertical
                if(b[i]==b[j]):
                    return False
                #diagonal
                #triangle, is height equal to width?
                '''
                e.g.
                [1,2]
                [1,4,3]
                [1,0,0,0]
                [0,0,0,1]
                [0,1,0,0]
                [0,0,0,0]

                [1,0,0,0]
                [0,0,1,0]
                [0,0,0,1]
                [0,0,0,0]
                equivalent to
                [1,3,4,0]
                b[i]=3 i=1
                b[j]=4 j=2
                height = 1
                width = 1
                height = 1+2
                width = 3+4
                '''
                height=abs(b[i]-b[j])
                width=abs(i-j)
                if(height==width):
                    return False
    return True
s = []
def nQueens(n):
    b=[0]*n
    #b=[1,0,0,3]
    # print(isValid(b))
    solve(n,b,1,0)
    return s

#what do we need to keep track of
#s append solutions, n size of board, 
#backtrack... when queen in current row is wrong.. go back and increment col
def solve(n, b, c, r):
    if(r<n and c<=n): #current row less than max length of board
        b[r]=c
        # if(b==[1,3,4,0]):
            # print('test')
        valid=isValid(b)
        if(r==n):
            if(valid):
                s.append(b)
        elif(valid):
            solve(n,b,1,r+1)
        elif(not valid and c<=n):
            solve(n,b,c+1,r)
        elif(not valid ): #back track
            solve(n,b,b[r-1]+1,r-1)
    elif(r<n): #backtrack #[2,4,1,3]
        b[r]=0
        solve(n,b,b[r-1]+1,r-1)
    elif(r==n):
        increment = False
        if(not b in s):
            increment = True
            valid=isValid(b)
            if(r==n):
                if(valid):
                    s.append(b)
            #increment = b[0]+1
            if(increment):
                b2=[0]*n
                b2[0]=b[0]+1
                solve(n,b2,1,1)

    

n=4
print(nQueens(n))

''' [1,3,4,2]
[1,0,0,0]
[0,0,1,0]
[0,0,0,1]
[0,1,0,0]
'''

'''[2,4,1,3]
[0,1,0,0]
[0,0,0,1]
[1,0,0,0]
[0,0,1,0]

'''
