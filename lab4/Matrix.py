#   Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. The class should
# provide methods to access elements (get and set methods) and some mathematical functions such as transpose,
# matrix multiplication and a method that allows iterating through all elements form a matrix an apply a
# transformation over them (via a lambda function).


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            print("Can't be multiplied.")
            return 0
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                value = 0
                for k in range(self.m):
                    value += self.get(i, k) * other.get(k, j)
                result.set(i, j, value)
        return result

    def transform(self, function):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, function(self.get(i, j)))
