from multimethod import multimethod
from helpers import HelperFunctions as hf

class BasicOperations:

    # function to add two elements
    @staticmethod
    def add_elements(a, b):
        return round(max(a, b), 6)
    
    # function to multiply two elements
    @staticmethod
    def multiply_elements(a, b):
        return round(a + b, 6)

    @multimethod
    @staticmethod
    def add(a, b: float):
        # a is list of lists
        # b is float
        # returns a list of lists
        c = []
        for i in range(len(a)):
            temp = []
            for j in range(len(a[i])):
                temp.append(a[i][j] + b)
            c.append(temp)
        return c
    
    @multimethod
    @staticmethod
    def add(a, b):
        # a and b are lists of lists
        # returns a list of lists
        c = []
        for i in range(len(a)):
            temp = []
            for j in range(len(a[i])):
                temp.append(float('-inf'))
            c.append(temp)

        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i][j] = BasicOperations.add_elements(a[i][j], b[i][j])

        return c
    
    @staticmethod
    def multiply(a, b):
        # a and b are lists of lists
        # returns a list of lists
        a_rows = len(a)
        a_columns = len(a[0])
        b_rows = len(b)
        b_columns = len(b[0])
        if a_columns != b_rows:
            raise ValueError("The number of columns of a is not equal to the number of rows of b")
        
        c = []
        for i in range(a_rows):
            temp = []
            for j in range(b_columns):
                temp.append(float('-inf'))
            c.append(temp)

        for i in range(a_rows):
            for j in range(b_columns):
                t = float('-inf')
                for k in range(a_columns):
                    t = BasicOperations.add_elements(BasicOperations.multiply_elements(a[i][k], b[k][j]), t)
                c[i][j] = t
        return c
    
    def fact(n):
        return n*(n+1)/2
    
    def maxEl(a):
        maxi = float('-inf')
        a_rows = len(a)
        a_columns = len(a[0])
        for i in range(a_rows):
            for j in range(a_columns):
                if a[i][j] > maxi:
                    maxi = a[i][j]
        return maxi
    
    @staticmethod
    def is_commutative(a, b):
        a_rows = len(a)
        a_columns = len(a[0])
        b_rows = len(b)
        b_columns = len(b[0])
        if a_columns != b_rows:
            raise ValueError("The number of columns of a is not equal to the number of rows of b")
        
        c = BasicOperations.multiply(a, b)
        d = BasicOperations.multiply(b, a)
        if c == d:
            return True
        else:
            return False
        
    def is_irreducible(a):
        a_rows = len(a)
        a_columns = len(a[0])
        # convert the matrix to an adjacency list
        adj_list = []
        for i in range(a_rows):
            temp = []
            for j in range(a_columns):
                if a[i][j] != float('-inf'):
                    temp.append(j)
            adj_list.append(temp)

        # create a visited array
        visited = [False for i in range(a_rows)]
        stack = []
        hf.dfs1(adj_list, visited, 0, stack)

        # make list of size a.rows
        adj_list1 = [[] for i in range(a_rows)]
        for i in range(a_rows):
            for j in range(a_columns):
                if a[i][j] != float('-inf'):
                    adj_list1[j].append(i)

        visited1 = [False for i in range(a_rows)]
        count = 0
        # traverse stack and call dfs2 for each element if not visited
        while stack:
            i = stack.pop()
            if not visited1[i]:
                count += 1
                if count > 1:
                    return False
                hf.dfs2(adj_list1, visited1, i)

        return True
    
    # @staticmethod
    def maper(a):
        # traverse through the matrix, takes one value from each rown and column and add them and
        # stores the combination with the maximum value
        if len(a) == 1:
            return a[0][0]
        
        import dlib   

        b = []
        for i in range(len(a)):
            temp = []
            for j in range(len(a[i])):
                # add the elements
                if(a[i][j] == float('-inf')):
                    temp.append(-1e15)
                else:
                    temp.append(a[i][j])
            b.append(temp)

        assignment = dlib.max_cost_assignment(dlib.matrix(b))
        # print(assignment)
        sum = 0
        for i in range(len(assignment)):
            sum += a[i][assignment[i]]

        return sum