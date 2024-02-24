# E = float('-inf')

from multimethod import multimethod 

# matrix class in python
class Matrix:
    def __init__(self, string, zeros = 0, rows = 0, columns = 0):   
        self.cycles = []
        self.critical_cycles = []
        # initialize empty eigenvalue
        self.eigen = float('-inf')
        if zeros == 1:
            self.rows = rows
            self.columns = columns
            self.matrix = [[float(0) for i in range(columns)] for j in range(rows)]
            return
        
        elif zeros == 2:
            self.rows = rows
            self.columns = columns
            self.matrix = [[float('-inf') for i in range(columns)] for j in range(rows)]
            return

        else:
            string = string[1:-1]
            # print(string)
            string = string.split(",")
            # print(string)
            self.matrix = []

            self.rows = len(string)
            self.columns = len(string[0].split(" "))
            for row in string:
                # removes leading spaces
                row = row.lstrip()
                row = row[1:-1]
                row = row.split(" ")
                # print(len(row))
                # print(row)
                # converts E to float('-inf')
                for i in range(len(row)):
                    if row[i] == "E":
                        row[i] = float('-inf')
                row = [float(i) for i in row]
                # print(row)
                self.matrix.append(row)
        # print(self.matrix) 
                
    def find_cycles(self):
        import networkx as nx
        edges = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != float('-inf'):
                    edges.append((i, j))
        # makes digraph using the edges
        G = nx.DiGraph(edges)

        self.cycles = list(nx.simple_cycles(G))

    def find_critical_cycles(self):
        maxi = float('-inf')
        for i in range(len(self.cycles)):
            temp = 0
            for j in range(len(self.cycles[i])):
                temp += self.matrix[self.cycles[i][j]][self.cycles[i][(j+1)%len(self.cycles[i])]]
            
            if temp/len(self.cycles[i]) > maxi:
                maxi = temp/len(self.cycles[i])
                self.critical_cycles.clear()
                self.critical_cycles.append(self.cycles[i])
            elif temp/len(self.cycles[i]) == maxi:
                self.critical_cycles.append(self.cycles[i])

        return maxi
    
    def eigenval(self):
        # checks if eigenvalue(self.eigen) is already present
        if(self.eigen != float('-inf')):
            return self.eigen
        if(self.cycles == []):
            self.find_cycles()
        # print(self.cycles)
        if(self.critical_cycles == []):
            self.eigen = self.find_critical_cycles()

        # print(self.critical_cycles)
        return self.eigen
    
    def eigenvec(self):
        # checks if eigenvalue(self.eigen) is already present
        if(self.eigen == float('-inf')):
            self.eigen = self.eigenval()

        a = Matrix("", 2, self.rows, self.columns)
        if(self.eigen > 0):
            a = subtract(self, self.eigen)

        # stores gamma
        g = gamma(a)
        # print_matrix(g)
        cols = []

        for i in range(len(self.critical_cycles)):
            temp = []
            for j in range(len(g.matrix)):
                temp.append(g.matrix[j][self.critical_cycles[i][0]])
            cols.append(temp)

        cols = find_distinct(cols)
        return cols
       
    
def print_matrix(a):
    for i in range(a.rows):
        for j in range(a.columns):
            print(a.matrix[i][j], end = " ")
        print()
    
# function to add two elements
def add_elements(a, b):
    return round(max(a, b), 6)

# function to multiply two elements
def multiply_elements(a, b):
    return round(a + b, 6)

# function to add two matrices
@multimethod
def add(a: Matrix, b: Matrix):
    if a.rows != b.rows or a.columns != b.columns:
        raise ValueError("The dimensions of the matrices are not equal")
    # creates an empty matrix
    c = Matrix("", 1, a.rows, a.columns)
    
    for i in range(a.rows):
        for j in range(a.columns):
            c.matrix[i][j] = add_elements(a.matrix[i][j], b.matrix[i][j])
    return c

# function to multiply two matrices
@multimethod
def multiply(a: Matrix, b: Matrix):
    if a.columns != b.rows:
        raise ValueError("The number of columns of a is not equal to the number of rows of b")
    # create an empty matrix
    c = Matrix("", 2, a.rows, b.columns)
    # for loop to iterate through the rows
    for i in range(a.rows):
        # for loop to iterate through the columns
        for j in range(b.columns):
            # for loop to iterate through the columns of a
            for k in range(a.columns):
                c.matrix[i][j] = add_elements(multiply_elements(a.matrix[i][k], b.matrix[k][j]), c.matrix[i][j])
    return c

@multimethod
def multiply(a: int, b: Matrix):
    # creates an empty matrix
    c = Matrix("", True, b.rows, b.columns)
    for i in range(b.rows):
        for j in range(b.columns):
            c.matrix[i][j] = multiply_elements(a, b.matrix[i][j])
    return c

@multimethod
def subtract(a: Matrix, b: float):
    # create an empty matrix
    c = Matrix("", True, a.rows, a.columns)
    for i in range(a.rows):
        for j in range(a.columns):
            c.matrix[i][j] = a.matrix[i][j] - b

    return c

# write a function to find the power of a matrix
def power(a, n):
    # check if the matrix is square
    if a.rows != a.columns:
        raise ValueError("The matrix is not square")
    c = a
    # multiply the matrix n-1 times
    for i in range(n-1):
        c = multiply(c, a)
    return c

def fact(n):
    return n*(n+1)/2

def maxEl(a: Matrix):
    maxi = float('-inf')
    for i in range(a.rows):
        for j in range(a.columns):
            if a.matrix[i][j] > maxi:
                maxi = a.matrix[i][j]
    return maxi

# @multimethod
def exp(a: Matrix):
    ans = subtract(a, 1)
    tempMat = a
    t = maxEl(a)
    # checks if t is float or int
    if t.is_integer():
        t = int(t)
    else:
        t = int(t) + 1

    # print(t)

    for i in range(t-1):
        tempMat = multiply(tempMat, a)
        divi = fact(i+2)
        # print(divi)
        ans = add(ans, subtract(tempMat, divi))

    return ans

# @multimethod
def exp(a: int):
    if(a < 1):
        return 0
    a_floor = int(a)
    ans = a_floor * a - fact(a_floor)
    return ans


def gamma(a : Matrix):
    tempMat = a
    ans = a
    # print_matrix(ans)
    for i in range(a.rows-1):
        tempMat = multiply(tempMat, a)
        ans = add(ans, tempMat)
    return ans

@multimethod
def subtract(a: list, b: list):
    # create an empty matrix
    c = []

    for i in range(len(a)):
        c.append(a[i] - b[i])
    return c

def find_distinct(cols):
    # print("Original cols:")
    # print(cols)
    remove = []
    n = len(cols)
    m = len(cols[0])
    # traverse cols. check if the index is not in remove
    for i in range(n):
        if i not in remove:
            for j in range(i+1, n):
                c = subtract(cols[i], cols[j])
                val = c[0]
                allsame = True
                for k in range(1, m):
                    if c[k] != val:
                        allsame = False
                        break
                if allsame:
                    remove.append(j)
    
    for i in sorted(remove, reverse=True):
        del cols[i]

    return cols

def maper(a: Matrix):
    # traverse through the matrix, takes one value from each rown and column and add them and
    # stores the combination with the maximum value
    import dlib   

    b = []
    for i in range(a.rows):
        temp = []
        for j in range(a.columns):
            # add the elements
            if(a.matrix[i][j] == float('-inf')):
                temp.append(-1e15)
            else:
                temp.append(a.matrix[i][j])
        b.append(temp)

    assignment = dlib.max_cost_assignment(dlib.matrix(b))
    # print(assignment)
    sum = 0
    for i in range(len(assignment)):
        sum += a.matrix[i][assignment[i]]

    return sum

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

    ans = (a + fact(c+1))/(c + 1)
    return round(ans, 6)

def is_commutative(a: Matrix, b: Matrix):
    if a.columns != b.rows:
        raise ValueError("The number of columns of a is not equal to the number of rows of b")
    
    c = multiply(a, b)
    d = multiply(b, a)
    if c.matrix == d.matrix:
        return True
    else:
        return False
    

# a = Matrix("[[4 4 3 8 1], [3 3 4 5 4], [5 3 4 7 3], [2 1 2 3 0], [6 6 4 8 1]]")
# b = Matrix("[[4 4 3 8 1], [3 3 4 5 4], [5 3 4 7 3], [2 1 2 3 0], [6 6 4 8 5]]")
# b = Matrix("[[18 17 16 16 15], [17 18 16 16 15], [15 15 18 18 17], [15 15 18 18 17], [16 16 19 19 18]]")
# a = Matrix("[[1 2 3]]")
# a = Matrix("[[2 4 2], [4 3 1], [2 1 3]]")
# a = Matrix("[[-3 -2 8], [1 0 4], [2 5 -6]]")
# a = Matrix("[[0 3 E E], [1 -1 E E], [E E 2 E], [E E E 1]]")
# a = Matrix("[[2 0 -1 3 1], [3 -1 1 2 0], [0 4 -1 2 1], [1 2 2 1 0], [-1 0 1 0 0]]")
# a = Matrix("[[3 6], [2 1]]")
# print_matrix(a)
# b = Matrix(2, 2)
# c = multiply(a, b)
# print_matrix(c)
# c = power(a, 2)

# c = a.eigenval()
# print("Eigenvalue is", c)
# d = a.eigenvec()
# print(d)
# a = 5 
# 3.66
# e = exp(3.8)
# print(e)
# log(5)
# e = maper(a)
# print(is_commutative(a, b))

# print(ev)
# print(c)
