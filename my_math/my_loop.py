from typing import Optional

def factorial(n: int) -> Optional[int]:
    if n >= 20:
        return None
    
    result = 1
    for i in range(2, n+1):
        result *= i

    return result

def gcd(a: int, b: int) -> Optional[int]:
    if a < 0 or b < 0:
        return None
    
    while (b != 0):
        a, b = b, a % b
    
    return a


class Diophantine():
    def __init__(self, x: int, y: int, solution: bool):
        self.x = x
        self.y = y
        self.has_solution = solution
        
    def __eq__(self, other) -> bool:
        return (self.x == other.x and 
            self.y == other.y and 
            self.has_solution == other.has_solution)
        

def extended_gcd_iterative(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    while b != 0:
        q = a // b
        a, b = b, a % b
        
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return x0, y0, a


def solve_diophantine(a: int, b: int, c: int) -> Diophantine:
    x, y, gcd = extended_gcd_iterative(a, b)
    
    if c % gcd == 0:
        return Diophantine(x * (c // gcd), y * (c // gcd), True)
    else:
        return Diophantine(0, 0, False)


