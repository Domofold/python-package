from typing import Optional, Tuple

def factorial(n: int) -> Optional[int]:
    if n >= 20:
        return None 
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1);
    

def gcd(a: int, b: int) -> Optional[int]:
    if a < 0 or b < 0:
        return None
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
class Diophantine():
    def __init__(self, x: int, y: int, solution: bool):
        self.x = x
        self.y = y
        self.has_solution = solution
    
    def __eq__(self, other) -> bool:
        return (self.x == other.x and 
            self.y == other.y and 
            self.has_solution == other.has_solution)
    
    
def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return (1, 0, a)
    x1, y1, gcd = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return (x, y, gcd)


def solve_diophantine(a: int, b: int, c: int) -> Diophantine:
    x, y, gcd = extended_gcd(a, b)
    if c % gcd == 0:
        return Diophantine(x * (c // gcd), y * (c // gcd), True)
    else:
        return Diophantine(0, 0, False)