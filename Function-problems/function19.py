# 19. Write a Python program to create Fibonacci series upto n using Lambda.


from functools import reduce

fibonacci_series = lambda x: reduce(lambda y, _: y + [y[-1] + y[-2]], range(x - 2), [0, 1])

print(fibonacci_series(7))
