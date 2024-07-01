# from matrix import Matrix
# from operations import Operations as op

class HelperFunctions:

    def __init__(self):
        # self.matrix = matrix
        self.cycles = []
        self.critical_cycles = []

    def find_cycles(self, matrix):
        if(self.cycles != []):
            return self.cycles

        import networkx as nx
        edges = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != float('-inf'):
                    edges.append((i, j))
        # makes digraph using the edges
        G = nx.DiGraph(edges)

        self.cycles = list(nx.simple_cycles(G))
        return self.cycles

    def find_critical_cycles(self, matrix):
        maxi = float('-inf')
        # if cycles are not present, find them
        if(self.cycles == []):
            self.find_cycles(matrix)
        for i in range(len(self.cycles)):
            temp = 0
            for j in range(len(self.cycles[i])):
                temp += matrix[self.cycles[i][j]][self.cycles[i][(j+1)%len(self.cycles[i])]]
            
            if temp/len(self.cycles[i]) > maxi:
                maxi = temp/len(self.cycles[i])
                self.critical_cycles.clear()
                self.critical_cycles.append(self.cycles[i])
            elif temp/len(self.cycles[i]) == maxi:
                self.critical_cycles.append(self.cycles[i])

        return (self.critical_cycles, maxi)
    
    def find_distinct(self, cols):
        # print("Original cols:")
        # print(cols)
        remove = []
        n = len(cols)
        m = len(cols[0])
        # traverse cols. check if the index is not in remove
        for i in range(n):
            if i not in remove:
                for j in range(i+1, n):
                    c = self.subtract(cols[i], cols[j])
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
    
    @staticmethod
    def dfs1(adj_list, visited, v, stack):
        visited[v] = True
        for i in adj_list[v]:
            if not visited[i]:
                HelperFunctions.dfs1(adj_list, visited, i, stack)
        stack.append(v)

    @staticmethod
    def dfs2(adj_list, visited, v):
        visited[v] = True
        for i in adj_list[v]:
            if not visited[i]:
                HelperFunctions.dfs2(adj_list, visited, i)

    @staticmethod
    def dfs3(adj_list, visited, v, temp):
        visited[v] = True
        temp.append(v)
        for i in adj_list[v]:
            if not visited[i]:
                HelperFunctions.dfs3(adj_list, visited, i, temp)

    def gcd(self, a, b):
        x = a
        y = b
        while(y):
            x, y = y, x % y
    
        return x
    
    def find_lcm(num1, num2):
        if(num1>num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while(rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2)/int(gcd))
        return lcm

    def lcm(l: list):
        num1 = l[0]
        if len(l) == 1:
            return num1
        num2 = l[1]
        lc = HelperFunctions.find_lcm(num1, num2)
        
        for i in range(2, len(l)):
            lc = HelperFunctions.find_lcm(lc, l[i])

        return lc

    def subtract(self, a: list, b: list):
        c = []

        for i in range(len(a)):
            c.append(a[i] - b[i])
        return c
    

