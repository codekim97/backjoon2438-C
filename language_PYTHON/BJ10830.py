#행렬 제곱
import sys


N,B = map(int,sys.stdin.readline().split())

initial_matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def multifly(m1,m2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += m1[i][k] * m2[k][j]
                result[i][j] = result[i][j] % 1000
    return result

def recursive(matrix,b):
    if b == 1:
        return matrix
    elif b % 2 == 0:
        matrix = recursive(matrix,b // 2)
        return multifly(matrix, matrix)
    else:
        matrix = recursive(matrix, b-1)
        return multifly(matrix, initial_matrix)

result_matrix = recursive(initial_matrix,B)

for i in range(N):
    for j in range(N):
        print(result_matrix[i][j] % 1000, end=" ")
    print()





# def multiplyMatrix(m1, m2):
#     length = len(m1)
#     result = [[0] * length for _ in range(length)]
#     for i in range(length):
#         for j in range(length):
#             for k in range(length):
#                 result[i][j] += m1[i][k] * m2[k][j]
#                 # 1000으로 나눠주면서 큰 수 연산을 줄인다.
#                 result[i][j] %= 1000
#     return result

# def recursivelyMultiplying(matrix, b):
#     if b == 1:
#         return matrix
#     else:
#         if b % 2 == 0:
#             matrix = recursivelyMultiplying(matrix,b // 2)
#             return multiplyMatrix(matrix, matrix)
        
#         else:
#             matrix = recursivelyMultiplying(matrix, b-1)
#             return multiplyMatrix(initial_matrix, matrix)

# n,b = map(int,sys.stdin.readline().split())
# initial_matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# result_matrix = recursivelyMultiplying(initial_matrix,b)

# for i in range(n):
#     for j in range(n):
#         print(result_matrix[i][j] % 1000, end=" ")
#     print()










