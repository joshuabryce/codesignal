import time

def sumSubsets(arr, num):
    solutions=set()
    sum=0
    subset=[]
    sumSubsetsR(arr, num, 0, solutions, sum, subset)
    stuff=[list(x) for x in solutions]
    stuff.sort()
    return stuff
    #print([list(x) for x in solutions])
    # return solutions

def sumSubsetsR(arrC, num, index, solutions, sum, subset):
    if(sum==num ): #and subset not in solutions):
        # append = True
        # for i in subset:
        #     if(lst[1:] == lst[:-1]):
        #         append = False
        #         break
        # if(append):
        subset.sort()
        solutions.add(tuple(subset))

    arr=arrC[:]
    for i in range(0,len(arr)):
        # if(i==index):
        #     continue
        if(arr[i]+sum<=num):
            arrR=arrC[:]
            temp=arrR.pop(i) #need to refactor this because it messes up the above for loop......
            subsetR=subset[:]
            subsetR.append(temp)
            sumSubsetsR(arrR, num, i, solutions, temp+sum, subsetR)
        else:
            break

test = [[1,1,2,4,4,4,7,13], 
 [1,1,2,4,4,4,20], 
 [1,1,2,4,4,9,15], 
 [1,1,2,4,9,19], 
 [1,1,2,4,13,15], 
 [1,1,2,7,9,16], 
 [1,1,2,13,19], 
 [1,1,2,16,16], 
 [1,1,4,4,4,7,15], 
 [1,1,4,4,4,9,13], 
 [1,1,4,4,7,19], 
 [1,1,4,4,13,13], 
 [1,1,4,15,15], 
 [1,1,9,9,16], 
 [1,1,15,19], 
 [1,2,4,4,7,9,9], 
 [1,2,4,4,9,16], 
 [1,2,4,7,9,13], 
 [1,2,4,9,20], 
 [1,2,4,13,16], 
 [1,2,7,13,13], 
 [1,2,9,9,15], 
 [1,2,13,20], 
 [1,4,4,4,7,16], 
 [1,4,4,7,20], 
 [1,4,7,9,15], 
 [1,4,9,9,13], 
 [1,4,15,16], 
 [1,7,9,19], 
 [1,7,13,15], 
 [1,9,13,13], 
 [1,15,20], 
 [1,16,19], 
 [2,4,4,4,7,15], 
 [2,4,4,4,9,13], 
 [2,4,4,7,19], 
 [2,4,4,13,13], 
 [2,4,15,15], 
 [2,9,9,16], 
 [2,15,19], 
 [4,4,4,9,15], 
 [4,4,9,19], 
 [4,4,13,15], 
 [4,7,9,16], 
 [4,13,19], 
 [4,16,16], 
 [7,9,20], 
 [7,13,16], 
 [16,20]]


expected = [[1, 1, 2, 4, 4, 4, 7, 13], [1, 1, 2, 4, 4, 4, 20], [1, 1, 2, 4, 4, 9, 15], [1, 1, 2, 4, 9, 19], [1, 1, 2, 4, 13, 15], [1, 1, 2, 7, 9, 16], [1, 1, 2, 13, 19], [1, 1, 2, 16, 16], [1, 1, 4, 4, 4, 7, 15], [1, 1, 4, 4, 4,
9, 13], [1, 1, 4, 4, 7, 19], [1, 1, 4, 4, 13, 13], [1, 1, 4, 15, 15], [1, 1, 9, 9, 16], [1, 1, 15, 19], [1, 2, 4, 4, 7, 9, 9], [1, 2, 4, 4, 9, 16], [1, 2, 4, 7, 9, 13], [1, 2, 4, 9, 20], [1, 2, 4, 13, 16], [1, 2, 7, 13, 13], [1, 2, 9, 9, 15], [1, 2, 13, 20], [1, 4, 4, 4, 7, 16], [1, 4, 4, 7, 20], [1, 4, 7, 9, 15], [1, 4, 9, 9, 13], [1, 4, 15, 16], [1, 7, 9, 19], [1, 7, 13, 15], [1, 9, 13, 13], [1, 15, 20], [1, 16, 19], [2, 4, 4, 4,
7, 15], [2, 4, 4, 4, 9, 13], [2, 4, 4, 7, 19], [2, 4, 4, 13, 13], [2, 4, 15, 15], [2, 9, 9, 16], [2, 15, 19], [4, 4, 4, 9, 15], [4, 4, 9, 19], [4, 4, 13, 15], [4, 7, 9, 16], [4, 13, 19], [4, 16, 16], [7, 9, 20], [7, 13, 16], [16, 20]]

print("test==expected ",test == expected)

start = time. time()
#"the code you want to test stays here"

arr= [1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20]
num= 36

print(sumSubsets(arr,num))

end = time. time()
print(end - start)