def uniqueValues(matrix):
    uniqueVals = []
    for j in range(len(matrix)):
        if j == 0:
            for i in range(len(matrix[j])):
                if matrix[j][i] not in uniqueVals:
                    uniqueVals.append(matrix[j][i])
        else:
            for z in uniqueVals:
                if z not in matrix[j]:
                    uniqueVals.pop(uniqueVals.index(z))
    return uniqueVals
    
newMatrix = []
size = input("Ingrese la cantidad de sublistas para la matriz: ")
while size.isdecimal() == False:
    size = input("Valor no valido, ingrese la cantidad de sublistas para la matriz: ")
size = int(size)
for i in range(size):
    newArr = []
    while (i != size):
        newVal = input(f"Ingrese un valor para la sublista numero {i + 1}: ")
        if newVal == "-1":
                break
        while newVal.isdecimal() == False:
            newVal = input(f"Valor no valido, ingrese un valor para la sublista numero {i + 1}: ")
        newVal = int(newVal)
        newArr.append(newVal)
    newMatrix.append(newArr)

print(uniqueValues(newMatrix))