

def findKnapsack(capacity, weight, value, size): 
  
    #Base Cases
    if size == 0:
        return 0
    if weight == 0:
        return 0
  
    #If weight of size's item is more than capacity, then not included
    if (weight[size-1] > capacity): 
        return findKnapsack(capacity, weight, value, size-1) 
  
    #Condition, sizeth item included or not included
    else: 
        return max(value[size-1] + findKnapsack(capacity-weight[size-1], weight, value, size-1), 
                   findKnapsack(capacity, weight, value, size-1)) 
  
    
#Main Code 
value = [10, 4, 3]
weight = [5, 4, 2]
capacity = 9
size = len(value)
print("Most valuable of subsets of items:",end= " ")
print(findKnapsack(capacity, weight, value, size))