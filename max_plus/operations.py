from multimethod import multimethod
from matrix import Matrix, zeros
from basicOperations import BasicOperations as bo
from helpers import HelperFunctions as hf
# from matrix import zeros

class MatrixOperations:

    @staticmethod
    def add_elements(a, b):
        return round(max(a, b), 6)
    
    @staticmethod
    def multiply_elements(a, b):
        return round(a + b, 6)

    # @multimethod
    @staticmethod
    def add(a: Matrix, b: Matrix):
        if a.rows != b.rows or a.columns != b.columns:
            raise ValueError("The dimensions of the matrices are not equal")

        c = zeros(a.rows, a.columns)
        
        for i in range(a.rows):
            for j in range(a.columns):
                c.matrix[i][j] = MatrixOperations.add_elements(a.matrix[i][j], b.matrix[i][j])
        return c
    
    @multimethod
    # @staticmethod
    def multiply(a: Matrix, b: Matrix):
        if a.columns != b.rows:
            raise ValueError("The number of columns of a is not equal to the number of rows of b")

        c = zeros(a.rows, b.columns)
        for i in range(a.rows):
            for j in range(b.columns):
                for k in range(a.columns):
                    c.matrix[i][j] = MatrixOperations.add_elements(MatrixOperations.multiply_elements(a.matrix[i][k], b.matrix[k][j]), c.matrix[i][j])
        return c

    @multimethod
    # @staticmethod
    def multiply(a: int, b: Matrix):
        c = zeros(b.rows, b.columns)
        for i in range(b.rows):
            for j in range(b.columns):
                c.matrix[i][j] = MatrixOperations.multiply_elements(a, b.matrix[i][j])
        return c

    # @multimethod
    @staticmethod
    def subtract(a: Matrix, b: float):
        c = zeros(a.rows, a.columns)
        for i in range(a.rows):
            for j in range(a.columns):
                c.matrix[i][j] = a.matrix[i][j] - b

        return c
    
    @staticmethod
    def power(a, n):
        # check if the matrix is square
        if a.rows != a.columns:
            raise ValueError("The matrix is not square")
        c = a
        for i in range(n-1):
            c = MatrixOperations.multiply(c, a)
        return c
    
    @multimethod
    # @staticmethod
    def exp(a: Matrix):
        ans = MatrixOperations.subtract(a, 1.0)
        tempMat = a
        t = bo.maxEl(a.matrix)
        # checks if t is float or int
        if t.is_integer():
            t = int(t)
        else:
            t = int(t) + 1

        # print(t)

        for i in range(t-1):
            tempMat = MatrixOperations.multiply(tempMat, a)
            divi = bo.fact(i+2)
            # print(divi)
            ans = MatrixOperations.add(ans, MatrixOperations.subtract(tempMat, divi))

        return ans

    @multimethod
    # @staticmethod
    def exp(a: float):
        if(a < 1):
            return 0
        a_floor = int(a)
        ans = a_floor * a - bo.fact(a_floor)
        return round(ans, 6)
    
    @staticmethod
    def log(a: int):
        from sympy import symbols, solve
        x = symbols('x')
        # solve the equation x^2 + x = 2a
        eq1 = x**2 + x - 2*a
        sol1 = solve(eq1)

        # eq2 = x**2 + 3*x + 2 - 2*a
        sol1 = [float(i) for i in sol1]
        c = 0
        # b = 0
        for i in sol1:
            if i > 0:
                # a = i
                c = int(i)

        ans = (a + bo.fact(c+1))/(c + 1)
        return round(ans, 6)
    
    @staticmethod
    def linear(a, b: list):
        
        a_rows = a.rows
        a_columns = a.columns

        if a_rows != len(b):
            raise ValueError("The number of rows of a is not equal to the length of b")
        
        c = []
        for i in range(a_rows):
            tempc = []
            for j in range(a_columns):
                tempc.append(a.matrix[i][j] - b[i])
                # c.matrix[i][j] = a.matrix[i][j] - b[i]
            c.append(tempc)

        # print_matrix(c)
        tempsoln = [float('-inf') for i in range(a_columns)]
        for i in range(len(c)):
            for j in range(len(c[i])):
                if c[i][j] > tempsoln[j]:
                    tempsoln[j] = c[i][j]

        for i in range(len(tempsoln)):
            if tempsoln[i] != 0:
                tempsoln[i] *= -1

        # print(tempsoln)
        M = []
        for i in range(a_columns):
            temp = []
            for j in range(a.rows):
                if -a.matrix[j][i] + b[j] == tempsoln[i]:
                    temp.append(j)
            M.append(temp)
        
        S = set()
        
        d = {}
        for i in range(len(M)):
            d[i] = 0

        # print(d)

        for i in range(len(M)):
            for j in range(len(M[i])):
                S.add(M[i][j])
                try:
                    d[M[i][j]] += 1
                except:
                    d[M[i][j]] = 1

        # print(S)

        for i in range(a.rows):
            if i not in S:
                return "No solution"
            
        # make empty string
        ans = ""
        for i in range(len(tempsoln)):
            if d[i] > 1:
                ans += "<=" + str(tempsoln[i]) + " "
            else:
                ans += str(tempsoln[i]) + " "
            
        return ans
    
    def characteristic(a: Matrix):
        import numpy as np
        from itertools import combinations
        m = np.array(a.matrix)
        n = a.rows
        # print(n)
        # make array on length a.rows
        deltas = np.zeros(n+1)
        for size in range(n-1, 0, -1):  # From n-1 down to 2 (if you want 2x2 submatrices)
            # submatrices = []
            sum = float('-inf')
            for rows in combinations(range(n), size):
                # for cols in combinations(range(n), n-size):
                submatrix = m[np.ix_(rows, rows)]
                sum = max(sum, bo.maper(submatrix))
                    # sum += bo.maper(submatrix)
            deltas[size] = sum

        deltas[n] = bo.maper(m)

        return deltas
    
    def period(a: Matrix):
        # instantiate the helper functions class
        hf1 = hf()
        if(bo.is_irreducible(a.matrix) == False):
            raise ValueError("The matrix is not irreducible")

        if a.rows != a.columns:
            raise ValueError("The matrix is not square")
        
        # find critical cycles in helper functions
        critical_cycles = hf1.find_critical_cycles(a.matrix)[0]
        # print(critical_cycles)
        
        adj_list = [[] for i in range(a.rows)]
        
        visEl = set()

        for i in range(len(critical_cycles)):
            for j in range(len(critical_cycles[i])):
                visEl.add(critical_cycles[i][j])
                adj_list[critical_cycles[i][j]].append(critical_cycles[i][(j+1)%len(critical_cycles[i])])
                adj_list[critical_cycles[i][(j+1)%len(critical_cycles[i])]].append(critical_cycles[i][j])

        # remove duplicates
        for i in range(a.rows):
            adj_list[i] = list(set(adj_list[i]))

        # print(adj_list)

        # dfs
        visited = [False for i in range(a.rows)]
        components = []
        for i in visEl:
            if not visited[i]:
                temp = []
                hf.dfs3(adj_list, visited, i, temp)
                components.append(set(temp))

        comp = len(components)
        gcds = [0 for i in range(comp)]
        # print(components)

        for i in range(len(critical_cycles)):
            el = critical_cycles[i][0] 
            for j in range(comp):
                if el in components[j]:
                    if gcds[j] == 0:
                        gcds[j] = len(critical_cycles[i])
                    else:
                        gcds[j] = hf.gcd(gcds[j], len(critical_cycles[i]))

        ans = hf.lcm(gcds)
        return ans
