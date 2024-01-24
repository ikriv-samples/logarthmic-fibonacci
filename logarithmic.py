from dataclasses import dataclass

@dataclass(frozen=True)
class Matrix:
    a11: int
    a12: int
    a21: int
    a22: int
   
    def __repr__(self):
        return f"Matrix({self.a11},{self.a12},{self.a21},{self.a22})"
    
    def __str__(self):
        return f"({self.a11},{self.a12},{self.a21},{self.a22})"
        
    def __getitem__(self, key):
       if key==0: return self.a11
       if key==1: return self.a12
       if key==2: return self.a21
       if key==3: return self.a22
       raise KeyError(key)
        
    def __mul__(self, other):
        return Matrix(
            self[0]*other[0] + self[1]*other[2],
            self[0]*other[1] + self[1]*other[3],
            self[2]*other[0] + self[3]*other[2],
            self[2]*other[1] + self[3]*other[3]
        )

def power(m: Matrix, n: int) -> Matrix:
    result=Matrix(1,0,0,1)
    currentPower=m
    while n>0:
        if n%2==1:
            result=result*currentPower
        n=n//2
        if n>0:
            currentPower=currentPower*currentPower
    return result

def fib(n: int) -> int:
    if n==0: return 0
    return power(Matrix(1,1,1,0), n-1)[0]
