#Methods 1 and 2 designed for 3 linear equations in 3 variables
def GaussJacobi():
    a1 = int(input("a1:"))
    a2 = int(input("a2:"))
    a3 = int(input("a3:"))
    b1 = int(input("b1:"))
    b2 = int(input("b2:"))
    b3 = int(input("b3:"))
    c1 = int(input("c1:"))
    c2 = int(input("c2:"))
    c3 = int(input("c3:"))
    d1 = int(input("d1:"))
    d2 = int(input("d2:"))
    d3 = int(input("d3:"))

    prevx = 0
    prevy = 0
    prevz = 0
    cx = 1
    cy = 1
    cz = 1
    counter=0
    while True:
        counter+=1
        cx = (d1-b1*prevy-c1*prevz)/a1
        cy = (d2-a2*prevx-c2*prevz)/b2
        cz = (d3-a3*prevx-b3*prevy)/c3
        if round(cx,2)==round(prevx,2):
            print(cx,cy,cz,counter)
            break
        else:
            prevx=cx
            prevy=cy
            prevz=cz
            print(cx,cy,cz,counter)
def GaussSeidle():
    a1 = int(input("a1:"))
    a2 = int(input("a2:"))
    a3 = int(input("a3:"))
    b1 = int(input("b1:"))
    b2 = int(input("b2:"))
    b3 = int(input("b3:"))
    c1 = int(input("c1:"))
    c2 = int(input("c2:"))
    c3 = int(input("c3:"))
    d1 = int(input("d1:"))
    d2 = int(input("d2:"))
    d3 = int(input("d3:"))

    prevx = 0
    prevy = 0
    prevz = 0
    cx = 1
    cy = 1
    cz = 1
    counter=0
    while True:
        counter+=1
        cx = (d1-b1*prevy-c1*prevz)/a1
        cy = (d2-a2*cx-c2*prevz)/b2
        cz = (d3-a3*cx-b3*cy)/c3
        if round(cx,2)==round(prevx,2):
            print(cx,cy,cz,counter)
            break
        else:
            prevx=cx
            prevy=cy
            prevz=cz
            print(cx,cy,cz,counter)
def eigstuff():
    import numpy as np
    a = int(input("Dimension of Square Matrix:"))
    M = np.zeros((a,a))
    for i in range(a):
        for j in range(a):
            inpstr = "x"+str(i+1)+str(j+1)+":"
            M[i,j] = float(input(inpstr))
    print("The Matrix is\n",M)
    vals = np.linalg.eigvals(M)
    print("The eigenvalues are\n",vals)
    print(np.linalg.eig(M))
def EchelonMatrix():
    import sympy as sp
    a = int(input("Dimension of Square Matrix:"))
    M = sp.zeros(a,a)
    for i in range(a):
        for j in range(a):
            inpstr = "x"+str(i+1)+str(j+1)+":"
            M[i,j] = float(input(inpstr))
    print("The echelon form is\n",M.rref())
    print("The rank is",M.rank())
def lineqnsolve():
    import numpy as np
    a = int(input("Dimension of Square Matrix:"))
    M = np.zeros((a,a))
    N = np.zeros((a,1))
    for i in range(a):
        for j in range(a):
            inpstr = "x"+str(i+1)+str(j+1)+":"
            M[i,j] = float(input(inpstr))
    print("The Matrix is\n",M)
    for i in range(a):
        str2 = "d"+str(i+1)+":"
        N[i,0]= float(input(str2))
    Minv = np.linalg.inv(M)
    X = np.matmul(Minv,N)
    print("The values of variables are\n",X)
def LUMatrix():
    from scipy.linalg import lu
    import numpy as np
    a = int(input("Dimension of Square Matrix:"))
    M = np.zeros((a,a))
    for i in range(a):
        for j in range(a):
            inpstr = "x"+str(i+1)+str(j+1)+":"
            M[i,j] = float(input(inpstr))
    print("The Matrix is\n",M)
    p,l,u = lu(M)
    print("L is \n",l)
    print("u is \n",u)
