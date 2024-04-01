from my_math import my_loop as ml
from my_math import my_recursion as mr

def test_gcd_iterative():
    assert ml.gcd(1 , 1) == 1
    assert ml.gcd(1, 2) == 1
    assert ml.gcd(2, 3) == 1
    assert ml.gcd(2, 4) == 2
    assert ml.gcd(12, 24) == 12
    assert ml.gcd(2137, 2137) == 2137

def test_factorial_iterative():
    assert ml.factorial(1) == 1
    assert ml.factorial(2) == 2
    assert ml.factorial(3) == 6
    assert ml.factorial(5) == 120
    assert ml.factorial(11) == 39916800
    
def test_diophantine_interative():
    
    assert(ml.solve_diophantine(3, -9, 3) == ml.Diophantine(1, 0, True))
    assert(ml.solve_diophantine(3, -6, 9) == ml.Diophantine(-3, -3, True))
    assert(ml.solve_diophantine(2, 2, 5) == ml.Diophantine(0, 0, False))
    assert(ml.solve_diophantine(200, 123, 333) == ml.Diophantine(2664, -4329, True))
    assert(ml.solve_diophantine(15, -10, 5) == ml.Diophantine(-1, -2, True))
    
def test_gcd_recursive():
    assert mr.gcd(1, 1) == 1
    assert mr.gcd(1, 2) == 1
    assert mr.gcd(2, 3) == 1
    assert mr.gcd(2, 4) == 2
    assert mr.gcd(12, 24) == 12
    assert mr.gcd(2137, 2137) == 2137

def test_factorial_recursive():
    assert mr.factorial(1) == 1
    assert mr.factorial(2) == 2
    assert mr.factorial(3) == 6
    assert mr.factorial(5) == 120
    assert mr.factorial(11) == 39916800
    
def test_diophantine_recursive():
    res = mr.solve_diophantine(2, 2, 5)
    print(f"{res.x}, {res.y}, {res.has_solution}")
    
    assert(mr.solve_diophantine(3, -9, 3) == mr.Diophantine(1, 0, True))
    assert(mr.solve_diophantine(3, -6, 9) == mr.Diophantine(-3, -3, True))
    assert(mr.solve_diophantine(2, 2, 5) == mr.Diophantine(0, 0, False))
    assert(mr.solve_diophantine(200, 123, 333) == mr.Diophantine(2664, -4329, True))
    assert(mr.solve_diophantine(15, -10, 5) == mr.Diophantine(-1, -2, True))