import random
# from properties import Properties
from basicOperations import BasicOperations as bo
from helpers import HelperFunctions

class Matrix:
    def __init__(self, string, randrange = False):   
        self.cycles = []
        self.critical_cycles = []
        # initialize empty eigenvalue
        self.eigenvalue = None
        self.eigenvector = None
        self.gam = None
        self.matrix = []
        self.hf = HelperFunctions()

        if(isinstance(string, list)):
            # self.matrix = string
            # string is a list of lists of ints. Convert to float and save in self.matrix
            for i in range(len(string)):
                temp = []
                for j in range(len(string[i])):
                    # check if string[i][j] == 'E' and convert to float('-inf')
                    if(string[i][j] == 'E'):
                        temp.append(float('-inf'))
                    else:
                        temp.append(float(string[i][j]))
                self.matrix.append(temp)
            self.rows = len(string)
            self.columns = len(string[0])
            return
        
        elif(isinstance(string, str)):
            # string will be given as "zero[rows, columns]" or "ones[rows, columns]" or "infs[rows, columns]"
            if(string[:4] == "zero"):
                self.rows = int(string[5])
                self.columns = int(string[7])
                for i in range(self.rows):
                    temp = []
                    for j in range(self.columns):
                        temp.append(0)
                    self.matrix.append(temp)
                return
            
            elif(string[:4] == "infs"):
                self.rows = int(string[5])
                self.columns = int(string[7])
                for i in range(self.rows):
                    temp = []
                    for j in range(self.columns):
                        temp.append(float('-inf'))
                    self.matrix.append(temp)
                return
            
            elif(string[:4] == "rand"):
                self.rows = int(string[5])
                self.columns = int(string[7])
                # check if randrange is given
                if(randrange != False):
                    # check if randrange is list or give error
                    if(isinstance(randrange, list)):
                        for i in range(self.rows):
                            temp = []
                            for j in range(self.columns):
                                temp.append(round(random.randint(randrange[0], randrange[1]), 6))
                            self.matrix.append(temp)
                        return
                    else:
                        raise ValueError("range not valid")
                    
                else:
                    for i in range(self.rows):
                            temp = []
                            for j in range(self.columns):
                                temp.append(round(random.random(), 6))
                            self.matrix.append(temp)
                    return
                
    # make __str__ method
    def __str__(self):
        # return string with newline characters except for last line
        s = ""
        for i in range(self.rows):
            for j in range(self.columns):
                s += str(self.matrix[i][j]) + " "
            if(i != self.rows-1):
                s += "\n"
        return s
                
    def eigenval(self):
        if(self.eigenvalue != None):
            return self.eigenvalue
        if(self.cycles == []):
            self.cycles = self.hf.find_cycles(self.matrix)
        # print(self.cycles)
        if(self.critical_cycles == []):
            ans = self.hf.find_critical_cycles(self.matrix)
            self.critical_cycles = ans[0]
            self.eigenvalue = ans[1]

        # print(self.critical_cycles)
        return self.eigenvalue
    
    def eigenvec(self):
        if(self.eigenvalue == None):
            self.eigenvalue = self.eigenval()

        a = self
        if(self.eigenvalue > 0):
            a.matrix = bo.add(a.matrix, -self.eigenvalue)

        # print("a:")
        # print(a.matrix)
        g = a.gamma().matrix
        # print("g:")
        # print(g)
        cols = []

        for i in range(len(self.critical_cycles)):
            temp = []
            for j in range(len(g)):
                temp.append(g[j][self.critical_cycles[i][0]])
            cols.append(temp)

        cols = self.hf.find_distinct(cols)
        return cols
    
    def gamma(self):
        # print("matrix:")
        # print(self.matrix)
        # if(self.gam != None):
        #     return self.gam
        tempMat = self
        ans = self
        # print_matrix(ans)s
        for i in range(self.rows-1):
            tempMat.matrix = bo.multiply(tempMat.matrix, self.matrix)
            # print("tempMat:")
            # print(tempMat.matrix)
            ans.matrix = bo.add(ans.matrix, tempMat.matrix)
        return ans
    
    def maper(self):
        # traverse through the matrix, takes one value from each rown and column and add them and
        # stores the combination with the maximum value
        import dlib   

        b = []
        for i in range(self.rows):
            temp = []
            for j in range(self.columns):
                # add the elements
                if(self.matrix[i][j] == float('-inf')):
                    temp.append(-1e15)
                else:
                    temp.append(self.matrix[i][j])
            b.append(temp)

        assignment = dlib.max_cost_assignment(dlib.matrix(b))
        # print(assignment)
        sum = 0
        for i in range(len(assignment)):
            sum += self.matrix[i][assignment[i]]

        return sum
    

    
def zeros(rows, columns):
    return Matrix("zero[{},{}]".format(rows, columns))

def infs(rows, columns):
    return Matrix("infs[{},{}]".format(rows, columns))

def rand(rows, columns, randrange = False):
    return Matrix("rand[{},{}]".format(rows, columns), randrange)

# a = Matrix([[-2, 1, 'E', -2], [-1, -3, -2, 'E'], ['E', -2, 0, 'E'], ['E', 'E', -2, -1]])
# print("gamma")
# print(a.gamma())