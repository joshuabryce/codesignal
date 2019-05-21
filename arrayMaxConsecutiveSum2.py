from copy import deepcopy
def arrayMaxConsecutiveSum2(inputArray):
    sol=0
    temp=[]
    start=0
    sum=0
    helper(inputArray,sol,temp,sum,start)
    return sol

def helper(inputArray,sol,temp,sum,start):
    print(start,sum,sol)
    if(start+1==len(inputArray)):
        return
    elif(inputArray[start]<0):
        start+=1
        sum=0
    if(start+1<len(inputArray)):
        sum+=inputArray[start]
        if sum > sol: 
            sol = sum
        helper(inputArray,sol,temp,sum,start+1)

inputArray= [-2, 2, 5, -11, 6]

print(arrayMaxConsecutiveSum2(inputArray))