def isPrime(num):
    if num <= 1: 
        return False
    for i in range(2, num, 1):
        if num % i == 0:
            return False
    return True

def sumValues(matrix):
    res = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            #print(f"{matrix[j][i]} es primo? {isPrime(matrix[j][i])}, y esta es la suma de sus index: {i + j}")
            if (j + i) % 2 != 0:
                if (isPrime(matrix[j][i])):
                    res += matrix[j][i] 
    return res

print(sumValues([[2,1,3],[31,7,8],[10,11,24]]))
