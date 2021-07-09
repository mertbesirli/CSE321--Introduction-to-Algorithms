

def findTotal(location,earn,temp,index,fix):
    #Check less than 4 km or not, then processing according to it.
    if len(location) == index:
        sum = 0
        if temp != None:
            for i in range(len(temp)-1):
                res = location[temp[i+1]] - location[temp[i]]
                if res < fix:
                    return 0
            for i in range(len(temp)):
                sum = sum + earn[temp[i]]
            return sum
        else:
            return 0
    #Return max value, recursively, firstly append to temp array
    else:
        temp.append(index)
        ret = max(findTotal(location, earn, temp[:-1], index+1,fix),findTotal(location, earn, temp[:], index+1,fix))
        return ret

def begin(location,earn):
    temp = []
    fix = 4
    resultMax = findTotal(location,earn,temp,0,fix)
    print("Maximize total:",end=" ")
    print(resultMax)

location = [1,2,3,4,5,6]
earn = [7,8,9,10,11,12]

begin(location,earn)