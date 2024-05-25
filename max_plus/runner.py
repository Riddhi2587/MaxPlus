from matrix import Matrix
from operations import MatrixOperations as mo
from matrix import zeros, infs, rand
power = mo.power
add = mo.add
multiply = mo.multiply
exp = mo.exp
linear = mo.linear
gamma = Matrix.gamma
char = mo.characteristic
linear = mo.linear
period = mo.period

def main():
    # a = Matrix([[0, 3, 'E', 'E'], [1, -1, 'E', 'E'], ['E', 'E', 2, 'E'], ['E', 'E', 0, 1]])
    # a = Matrix([[0, 3, 'E', 0], [1, -1, 0, 'E'], ['E', 0, 2, 'E'], ['E', 'E', 0, 1]])
    # print(a.eigenval())
    a = Matrix([[2, 1, 4], [1, 0, 1], [2, 2, 1]])
    # print(period(a))
    # print(char(a))
    # b = [3, 1, 2]
    # print(linear(a, b))
    
    # print(a.eigenval())
    # print(a.eigenvec())
    # print(a.maper())
    # print(exp(a))
    # print(exp(2.5))
    # print(a.gamma())

    # b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(multiply(a, b))
    # print(add(a, b))
    # b = zeros(3, 3)
    # b = infs(3, 3)
    # b = rand(3, 3, [0, 10])
    # print(b)

main()
