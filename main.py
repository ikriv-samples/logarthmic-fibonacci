import sys
sys.set_int_max_str_digits(1_000_000)
argv = sys.argv
algo, n = argv[1:] if len(argv)==3 else ("logarithmic", argv[1])
print(__import__(algo).fib(int(n)))

