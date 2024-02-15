To initialize a matrix 

a = Matrix("[[2 4 2], [4 3 1], [2 1 3]]")

Functions:

1. Add
   If a and b are 2 matrices, 
   c = add(a, b)
   To view c,
   print_matrix(c)

2. Multiply
   If a and b are 2 matrices, 
   c = multiply(a, b)
   To view c,
   print_matrix(c)

   If a is a matrix and b is a scalar
   c = multiply(b, a)
   To view c,
   print(c)

3. Power
   c = power(a, n)
   To view c,
   print_matrix(c)

4. Exponent
    If a is a matrix
    c = exp(a)
    print_matrix(c)

    If a is a scalar
    c = exp(a)
    print(a)
    

5. Gamma
    c = gamma(a)
    print_matrix(c)

6. Permanent
    c = maper(a)
    print(c)

7. Eigenvalue
    c = a.eigenval()
    print(c)

8. Eigenvec
    c = a.eigenvec()
    print(c)