
#Display of array
def display(sub):
    print(sub)
#Array of letters process with dynamicly
def solve(arr,temp,index):
    if index == len(arr):
        subArray = []
        for l in temp:
            x = (temp[l]/2)
            if x >= 1:
                for i in range(int(temp[l] / 2)):
                    subArray.insert(0,l)
                    subArray.append(l)
                    temp[l] = temp[l] - 2
        for l in temp:
            if temp[l] == 1:
                subArray.insert(int(len(subArray)/2),l)
                break
        display(subArray)
        return subArray
    else:
        if arr[index] in temp:
            temp[arr[index]] = temp[arr[index]] + 1
        else:
            temp[arr[index]] = 1
        solve(arr, temp, index+1)
        
def begin(arr):
    temp= {}
    solve(arr,temp,0)
    
def test1():
    print("Result:",end=" ")
    arr = ['a','m','i','s','i','a','b']
    begin(arr)
    
def test2():
    print("Result:",end=" ")
    arr = ['a','b','e','a','d','r','t','t','a']
    begin(arr)

test1()
test2()