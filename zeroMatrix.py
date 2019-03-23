'''
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
'''
import numpy as np

def zeroedMatrix(matrix,size):
    zero_indices = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                zero_indices.append((i,j))
    
    for indices in zero_indices:
        matrix[indices[0],:] = 0
        matrix[:,indices[1]] = 0

    print("Zeroed Matrix :{0}".format(matrix))


if __name__ == '__main__':
    size = int(input())
    matrix = np.random.randint(3,size=(size,size))
    print('Original Matrix : {0}'.format(matrix))
    zeroedMatrix(matrix,size)