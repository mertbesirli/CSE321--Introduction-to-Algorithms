

def minimumSumPath(A): 
      
    #For storing the result in array
    memo = [None] * len(A) 
    n = len(A) - 1
      
    #For the bottom row 
    for i in range(len(A[n])):  
        memo[i] = A[n][i]  
  
    #Calculation of the remaining rows in bottom up.
    for i in range(len(A) - 2, -1,-1):  
        for j in range( len(A[i])):  
            memo[j] = A[i][j] + min(memo[j], memo[j + 1])
  
    #Return the top element 
    return memo[0] 
  
A = [[ 2 ], 
    [5, 4 ], 
    [1, 4, 7],
    [8,6,9,6]]; 
#Printing to minimum summation path
print("Minimum Sum path is:",end=" ")
print(minimumSumPath(A)) 