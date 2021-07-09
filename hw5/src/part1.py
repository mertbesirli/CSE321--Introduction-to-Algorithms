
# The vector v stores current subset. 
def findSubsetDynamic(arr,size,v,sum,count) :
    #Base case
    if size == count:
        sum = 0
        for item in v:
            sum = sum + item
        length = len(v)
        #Print subset of sum
        if sum == 0 and length != 0:
            print(v, end=" ")
        return True
    else:
        findSubsetDynamic(arr,size,v[:],sum,count+1)
        v.append(arr[count])
        findSubsetDynamic(arr,size,v[:],sum,count+1)
  
# Wrapper over printAllSubsetsRec() 
def first(arr,size,sum): 
    v = []
    findSubsetDynamic(arr,size,v,sum,0)
    
arr = [2, 3, -5, -8, 6, -1] 
sum = 0
size = len(arr)
print("Each subsets are:",end=" ")
first(arr,size,sum)
  