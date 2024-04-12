def intersect(arr1, arr2):
    newArr = []
    for i in range(len(arr1)):
            if (arr1[i] in arr2 and arr1[i] not in newArr):
                newArr.append(arr1[i])

    return newArr

print(intersect([1,2,3,3,4,5],[3,4,5,6,7]))