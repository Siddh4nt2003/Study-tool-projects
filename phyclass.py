def scinotat(x):
    num = x
    count10 = 0
    while num<10:
        num = num*10
        count10 +=1
        if num>1 and num<10:
            break

    print(round(num,2),"x","10^",-count10)
def elecEnergy():
    a = float(input("box width:"))
    n= int(input("Energy level"))
    h = 6.63e-34
    m = 9.1e-31
    E = (n*h)**2/(8*m*(a**2))
    P = (2*m*E)**0.5
    wlen = h/P
    print("The Energy of e is:")
    scinotat(E)
    print("The wavelength is")
    scinotat(wlen)
def lcrcircuit():
    from math import sqrt
    V = float(input("Peak Voltage:"))
    w = float(input("w/Angular velocity:"))
    R = float(input("Resistance:"))
    L = float(input("Inductance:"))
    C = float(input("Capacitance:"))
    Xl = w*L
    if C!=0:
        Xc = 1/(w*C)
    else:
        Xc = 0
    Z = sqrt(R**2+(Xl-Xc)**2)
    print("The impedance is",round(Z,2),"ohms")
    Pfactor = R/Z
    print("Power Factor is",Pfactor)
    Im = V/Z
    print("Imax = ",round(Im,2),"A")
    P = V*Im*Pfactor/2
    print("Power is ",round(P,2),"W")
def elecprob():
    from scipy.integrate import quad
    from math import pi
    from numpy import sin
    a = float(input("Total width in Amstrong:"))
    l = float(input("lower limit:"))
    u = float(input("Upper limit:"))
    n = int(input("Energy level:"))
    def f(x):
        return 2*((sin(n*pi*x/a))**2)/a
    P = quad(f,l,u)
    print("The probability is",round(P[0],4))
def heisenberg():
    #delx*delp=h/4pi
    from math import pi
    choice = int(input("To find : 1.delx 2.delp 3.delv"))
    h = 6.63e-34
    if choice==1:
        delp = float(input("delp:"))
        delx = h/(4*pi*delp)
        print("delx is:")
        scinotat(delx)
    elif choice==2:
        delx = float(input("delx:"))
        delp = h/(4*pi*delx)
        print("delp is:")
        scinotat(delp)
    elif choice==3:
        m = float(input("m:"))
        delx = float(input("delx:"))
        delv = h/(4*pi*delx*m)
        print("delv is")
        scinotat(delv)
def resistivity():
    from sympy import Symbol,solve
    #rho = m/ne*e*t
    rho = Symbol('rho')
    tmp = input(rho)
    if tmp!='na':
        rho = float(tmp)
    n = Symbol('n')
    tmp = input(n)
    if tmp!='na':
        n= float(tmp)
    t = Symbol('T')
    tmp = input(t)
    if tmp!='na':
        t = float(tmp)
    m = 9.1e-31
    e = 1.6e-19
    eq = rho-(m/(n*e*e*t))
    l1 = [rho,n,t]
    for i in l1:
        if type(i) is not float:
            print(solve(eq,i))
            break
def moles():
    from sympy import Symbol,solve
    #n = dNa/Mat
    Na = 6.022e23
    M = Symbol('M')
    tmp = input(M)
    if tmp!='na':
        M = float(tmp)
    n = Symbol('n')
    tmp = input(n)
    if tmp!='na':
        n= float(tmp)
    d = Symbol('d')
    tmp = input(d)
    if tmp!='na':
        d = float(tmp)
    eq = n-d*Na/M
    l1 = [M,n,d]
    for i in l1:
        if type(i) is not float:
            print(solve(eq,i))
            break
def driftvelo():
    from sympy import Symbol,solve
    #v = eEt/m
    E = Symbol('E')
    tmp = input(E)
    if tmp!='na':
        E = float(tmp)
    v = Symbol('v')
    tmp = input(v)
    if tmp!='na':
        v = float(tmp)
    t = Symbol('T')
    tmp = input(t)
    if tmp!='na':
        t = float(tmp)
    m = 9.1e-31
    e = 1.6e-19
    eq = v - e*E*t/m
    l1 = [E,v,t]
    for i in l1:
        if type(i) is not float:
            print(solve(eq,i))
            break
def conductivity():
    from sympy import Symbol,solve
    #rho = m/ne*e*t
    sigma = Symbol('sigma')
    tmp = input(sigma)
    if tmp!='na':
        sigma = float(tmp)
    n = Symbol('n')
    tmp = input(n)
    if tmp!='na':
        n= float(tmp)
    t = Symbol('T')
    tmp = input(t)
    if tmp!='na':
        t = float(tmp)
    m = 9.1e-31
    e = 1.6e-19
    eq = sigma-((n*e*e*t)/m)
    l1 = [sigma,n,t]
    for i in l1:
        if type(i) is not float:
            print(solve(eq,i))
            break
