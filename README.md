Logarithmic Fibonacci
==========
# TL;DR
Fibonacci sequence is defined as a sequence starting with 0, 1 where each subsequent member is calculated as `fib(n) = fib(n-1)+fib(n-2)`. This yields an infinite sequence 0, 1, 1, 2, 3, 5, 8, 13, ... 

This repository compares several approaches to calculating n*th* Fibonacci number:
* A naive recursive solution
* A simple linear solution
* A solution that runs in logarithmic time

# Running The Samples
`python main.py {algorithm} n`
Algorithm can be one of `linear`, `recursive`, or `logarithmic`.
If algorithm is omitted, `logarthmic` is used.

# Naive Solution
It is very easy to program Fibonacci sequence exactly as defined, but it leads to a slow and inefficient solution:
```python
def fib(n: int) -> int:
    if n==0: return 0
    if n==1: return 1
    return fib(n-1)+fib(n-2)
```
This solution has exponential runtime, so it hits extremely long calculation times for relatively small values of n. On my machine `python main.py recursive 40` takes over 20 seconds.
# Linear Solution
```python
def fib(n: int) -> int:
    if n==0: return 0
    if n==1: return 1
    prev,current=0,1
    for i in range(n-1):
       prev,current=current,prev+current
    return current
```
This solution works well up to n=100,000 or so, but then it starts to lag.
# Logarithmic Solution
This solution is based on the fact that 2x2 matrix
```
    | 1    1 |
A = |        |
    | 1    0 |
```
when raised to the power of n yields
```
        | fib(n+1) fib(n)   |
A**n == |                   |
        | fib(n)   fib(n-1) |
```
## Proof
The above property can be proved by induction. It is obviously true for n=1.
Now, supposed it is true for n=k, so
```
        | fib(k+1) fib(k)   |
A**k == |                   |
        | fib(k)   fib(k-1) |
```
Then `A**(k+1)` is `(A**k)*A`, or
```
           | fib(k+1) fib(k)   |   | 1   1 |    | fib(k+1)+fib(k)    fib(k+1) |
A**(k+1) = |                   | * |       | == |                             |
           | fib(k)   fib(k-1) |   | 1   0 |    | fib(k)+fib(k-1)    fib(k)   |
```
Simplifying this, we get
```
           | fib(k+2)  fib(k+1) |
A**(k+1) = |                    |
           |  fib(k+1)  fib(k)  |
```
So, the property is proved by induction.
## OK, we proved it. So?

We can exploit the fact that matrix multiplication is associative to make the number of computations logarithmic. If n is a power of 2, we can compute A**n in log2(n) steps. For example, if n=16, we can compute it in 4 steps:
```
A2=A*A
A4=A2*A2
A8=A4*A4
A16=A8*A8
```
If n is not a power of 2, we will assemble A**n from parts using binary representation of n:
```
n = 11 == 1011b
A2=A*A
A4=A2*A2
A8=A4*A4
An=A*A2*A8
```
We can build the result gradually, there is no need to keep the intermediate values:
```
result=A
A2=A*A
result=result*A2
A4=A2*A2
A8=A4*A4
result=result*A8
```
The complete generalized code is in `logarithmic.py`.
## Execution Times
Recursive approaches runtime increases exponentially. It becomes over 20 seconds for n=40.
Linear approach works well up to n~=100,000.
Logarithmic approach can calculate value of fib(10_000_000) in a few seconds.
We must remember that logarithmic approach is logarithmic only in terms of the number of Python integer multiplications. Since Python integers have arbitrary length, multiplications get slower and slower as the numbers become bigger, so the actual wall clock times will not be truly logarithmic.
