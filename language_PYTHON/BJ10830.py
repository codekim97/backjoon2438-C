#행렬 제곱
import sys

def multiplyMatrix(m1, m2):
    length = len(m1)
    result = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += m1[i][k] * m2[k][j]
                # 1000으로 나눠주면서 큰 수 연산을 줄인다.
                result[i][j] %= 1000
    return result

def recursivelyMultiplying(matrix, b):
    if b == 1:
        return matrix
    else:
        if b % 2 == 0:
            matrix = recursivelyMultiplying(matrix,b // 2)
            return multiplyMatrix(matrix, matrix)
        
        else:
            matrix = recursivelyMultiplying(matrix, b-1)
            return multiplyMatrix(initial_matrix, matrix)

n,b = map(int,sys.stdin.readline().split())
initial_matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result_matrix = recursivelyMultiplying(initial_matrix,b)

for i in range(n):
    for j in range(n):
        print(result_matrix[i][j] % 1000, end=" ")
    print()







# graph = []
# answer = [[0 for _ in range(N)] for _ in range(N)]
# #행렬에 값넣기
# for i in range(N):
#     graph.append(list(map(int,sys.stdin.readline().rstrip().split())))


# def double(n,b):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 answer[i][j] += graph[i][k] * graph[k][j]

# double(N,B)
# for i in answer:
#     print(i)


# import sys
 
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
#             matrix = recursivelyMultiplying(matrix, b // 2)
#             return multiplyMatrix(matrix, matrix)
 
#         else:
#             matrix = recursivelyMultiplying(matrix, b-1)
#             return multiplyMatrix(initial_matrix, matrix)
 
# n, b = map(int, sys.stdin.readline().split())
# initial_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# result_matrix = recursivelyMultiplying(initial_matrix, b)
# for i in range(n):
#     for j in range(n):
#         print(result_matrix[i][j] % 1000, end = ' ')
#     print()