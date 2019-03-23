'''
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
'''
import numpy as np

def rotateMatrix(matrix,size):
    for i in range(int(size/2)):
        for j in range(i,size-1-i):
            tmp = matrix[i][j]

            matrix[i][j] = matrix[size-1-j][i]
            matrix[size-1-j][i] = matrix[size-1-i][size-1-j]
            matrix[size-1-i][size-1-j] = matrix[j][size-1-i]
            matrix[j][size-1-i] = tmp
    
    print("Rotated Matrix :{0}".format(matrix))


if __name__ == '__main__':
    size = int(input())
    matrix = np.random.randint(10,size=(size,size))
    print('Original Matrix : {0}'.format(matrix))
    rotateMatrix(matrix,size)